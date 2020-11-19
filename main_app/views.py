from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from login_reg_app.models import *
from .models import *
from django.db.models import Q
# from django.views.generic.list import ListView
from django.views.generic import ListView
from itertools import chain


def index(request):
    #project = Project.objects.get(len(watchers))
    context = {
        "all_projects": Project.objects.all(),
        # 'top_projects': project[:5] 
    }
        
    return render(request, 'index.html', context)

def dashboard(request):

    if 'role' not in request.session:
        return redirect('/')

    if request.session['role'] == 'client':
        user = Client.objects.get(id=request.session['client_id'])
        
        context = {
            'user': user,
            'my_watchlists': Project.objects.filter(watchers=request.session['client_id']),
            "all_projects": Project.objects.all(),
            
        }
        return render(request, 'dashboard.html', context)
        
    ######### Changed to else, try running code now #########    
    else:
        request.session['role'] == 'dev'
        user = Dev.objects.get(id=request.session['dev_id'])
        context = {
            'user': user,
            'my_projects': Project.objects.filter(creator=request.session['dev_id']),
            "all_projects": Project.objects.all(),
        }
        return render(request, 'dashboard.html', context)

def show_dev(request, dev_id):
    context = {
        'dev' : Dev.objects.get(id = dev_id)
    }
    return render(request, 'dev_profile.html', context)

def show_project(request, project_id):
    if request.session['role'] == 'client':
        user = Client.objects.get(id=request.session['client_id'])
    else:
        user = Dev.objects.get(id=request.session['dev_id'])
    

    this_project = Project.objects.get(id=project_id)
    
    views = this_project.times_viewed + 1

    context = {
        'project' : this_project,
        'user' : user,
        'views': views,
        }    
    return render(request, 'project.html', context)


def add_project(request):

    if request.session['role'] == 'client':
        user = Client.objects.get(id=request.session['client_id'])
    elif request.session['role'] == 'dev':
        user = Dev.objects.get(id=request.session['dev_id'])
    context = {
        'user': user,
    }

    return render(request, 'upload_project.html', context)

def create_project(request):
    form = request.POST
    new_project = Project.objects.create(
        name = form['proj_name'],
        pitch = form['quick_pitch'],
        about = form['desc'],
        category = form['category'],
        price = form['price'],
        creator = Dev.objects.get(id=request.session['dev_id'])
    )
    project_id = new_project.id
    return redirect('/dashboard')

# def upload_proj_img(request,project_id):
#     context = {
#         'project' : Project.objects.get(id = project_id)
#     }
#     return render(request, 'project_image.html', context)

######### Add project Image ##########
# def add_project_img(request, project_id):
#     project = Project.objects.get(id = project_id)
#     pic = Project_Image.objects.create(
#         image = request.FILES['image'],
#         project_pic = project,
#     )
#     return redirect('/dashboard')

def add_to_watchlist(request, project_id):
    added_project = Project.objects.get(id = project_id)
    user = Client.objects.get(id=request.session['client_id'])
    added_project.watchers.add(user)
    return redirect('/dashboard')
    
def remove_from_watchlist(request, project_id):
    removed_project = Project.objects.get(id=project_id)
    user = Client.objects.get(id=request.session['client_id'])
    removed_project.watchers.remove(user)
    return redirect('/dashboard')
    
def delete_project(request, project_id):
    proj = Project.objects.get(id=project_id)
    proj.delete()
    return redirect('/dashboard')

def edit_project(request, proj_id):
    form = request.POST
    proj = Project.objects.get(id=proj_id)
    proj.name = form['proj_name']
    proj.pitch = form['pitch']
    proj.about = form['desc']
    proj.category = form['category']
    proj.price = form['price']
    proj.save()
    return redirect('/dashboard')

########## Add Dev Image ##########
# def add_user_img(request):
#   dev = Dev.objects.get(id = request.session['user_id'])
#   pic = Dev.profile_pic.update(profile_pic = request.FILES['profile_pic'])
#   return redirect('/back to profile)
#

#     ----->Messageing Area<-----

# def inbox(request, user_id):

#     if request.session['role'] == 'client':
#         user = Client.objects.get(id=request.session['client_id'])
#     elif request.session['role'] == 'dev':
#         user = Dev.objects.get(id=request.session['dev_id'])


#     context = {
#         'user': user,
#         "all_devs": Dev.objects.all(),
#         'sent_messages': Chat.objects.all()
#     }
#     return render(request, 'inbox.html', context)

# def new_chat(request):
#     form = request.POST
#     user = Dev.objects.get(id=form['user_id'])
#     sent_to = Dev.objects.get(id=form['other_dev_id'])
#     Chat.objects.create(
#         text = form['text'],
#         starter = user,
#         messager = form['dev_id']
#     )
#     return redirect(f'inbox/{form['user_id']}')

# def new_reply(request):
#     form = request.POST
#     convo = Chat.objects.get(id=form['message.id'])
#     user = Dev.objects.get(id=form['user.id'])
#     Reply.objects.create(
#         post = form['post'],
#         replier = user,
#         convo = convo
#     )
#     return render(request, 'about.html')

#       ----->End Message Area<-----

#       ----->search bar<-----

class SearchBar(ListView):
    template_name = 'search_view.html'
    paginate_by = 20
    count= 0
    print(9)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        print(8)
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            print(7)
            dev_results = Dev.objects.search(query)
            project_results = Project.objects.search(query)
            queryset_chain = chain(
                dev_results,
                project_results,
                )
            qs = sorted(queryset_chain,
                key=lambda instance: instance.pk,
                reverse=True)
            self.count = len(qs)
            return qs
            print(6)
        return Dev.objects.none()

def about(request):
    return render(request, 'about.html')

def logout(request):
    request.session.flush()
    return redirect('/')


######### INFO YOU NEED TO KNOW ABOUT LOGGED IN USER ############


# all users will have a role stored in session, as either 'dev' or 'client'
    # request.session['role'] = 'client' / 'dev'

# you can check to see if a user is logged in by:
    # if 'role' not in request.session:
        # do x or whatever

# depending on the role, they will either have a 'client_id' or 'dev_id'
    # request.session['client_id']
    # request.session['dev_id]

# so you can get your user's object by doing this:
    # check if user is dev or client first
        #if request.session['role'] == 'client' (or 'dev')
    # Client.objects.get(id=request.session['client_id'])
    # Dev.objects.get(id=request.session['dev_id])


# def category_search_button(request, category):
#     context = {
#       "category" : Project.objects.filter(category = category).all()
#     }
#     return render(request, "category.html", context)