from django.shortcuts import render, redirect
from .models import Client, Dev
from django.contrib import messages
import bcrypt


# Create your views here.
def login_reg(request):
    context = {
        'all_clients': Client.objects.all(),
        'all_devs': Dev.objects.all(),
    }
    return render(request, 'login_reg.html', context)

def register(request):
    errors = Client.objects.registration_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/login_reg')
    if Client.objects.filter(email=request.POST['email']) or Dev.objects.filter(email=request.POST['email']):
        messages.error(request, "An account with that email already exists")
        return redirect('/login_reg')
    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    
    if request.POST['role'] == 'client':
        this_client = Client.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = hashed_pw
        )
        request.session['role'] = 'client'
        request.session['client_id'] = this_client.id

    elif request.POST['role'] == 'dev':
        this_dev = Dev.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = hashed_pw
        )
        request.session['role'] = 'dev'
        request.session['dev_id'] = this_dev.id

    return redirect('/login_reg/success')

def login(request):
    if request.POST['role'] == 'client':
        client_get = Client.objects.filter(email=request.POST['email'])
        if client_get:
            this_client = client_get.first()
            if bcrypt.checkpw(request.POST['password'].encode(), this_client.password.encode()):
                request.session['role'] = 'client'
                request.session['client_id'] = this_client.id
                return redirect('/login_reg/success')
    elif request.POST['role'] == 'dev':
        dev_get = Dev.objects.filter(email=request.POST['email'])
        if dev_get:
            this_dev = dev_get.first()
            if bcrypt.checkpw(request.POST['password'].encode(), this_dev.password.encode()):
                request.session['role'] = 'dev'
                request.session['dev_id'] = this_dev.id
                return redirect('/login_reg/success')
    messages.error(request, "Login failed - check your email or password")
    return redirect('/login_reg')

def success(request):
    return redirect('/dashboard')

def new_chat(request):
    pass

def logout(request):
    request.session.flush()
    return redirect('/')

def delete(request, role, user_id):
    if role == 'client':
        Client.objects.get(id=user_id).delete()
    if role == 'dev':
        Dev.objects.get(id=user_id).delete()
    return redirect('/login_reg')



