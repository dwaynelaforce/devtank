from django.shortcuts import render, redirect
from login_reg_app.models import *
from .models import *

def index(request):
    # if 'role' not in request.session:
    #     render normal html
    # elif request.session['role'] == 'client'
    #     do this

    context = {
        'projects': Project.categories.all(),        
    }
        
    
    return render(request, 'index.html')

def dashboard(request):

    if 'role' not in request.session:
        return redirect('/')

    if request.session['role'] == 'client':
        user = Client.objects.get(id=request.session['client_id'])
    elif request.session['role'] == 'dev':
        user = Dev.objects.get(id=request.session['dev_id'])
    context = {
        'user': user,
    }

    return render(request, 'dashboard.html', context)

def add_project(request):
    return render(request, 'upload_proj.html')

def create_project(request):
    form = request.POST
    Project.objects.create(
        name = form['proj_name'],
        pitch = form['quick_pitch'],
        about = form['desc'],
        category = form['category'],
        price = form['price'],
        creator = Dev.objects.get(id=form['creator'])
    )
    return redirect('/dashboard')

########## Add Dev Image ##########
# def add_user_img(request):
#   dev = Dev.objects.get(id = request.session['user_id'])
#   pic = Dev.profile_pic.update(profile_pic = request.FILES['profile_pic'])
#   return redirect('/back to profile)
#



########## Add project Image ##########
# def add_project_img(request):
#     project = Project.objects.get(id = request.POST['project'])
#     pic = Project_Image.objects.create(
#         image = request.FILES['image']
#         project = project
#     )
#     return redirect('/some path to the project')

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
#     return render(request, "category.html",context)