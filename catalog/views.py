from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import RegistrationForm

def registration(request):
    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            context['success'] = 'user successfully created'
            render(request, 'catalog/login.html', context)

    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, 'catalog/registration.html', context)

def login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/o/applications')
            else:
                context['message'] = 'user blocked'
        else:
            context['message'] = 'username or password invalid'

    return render(request, 'catalog/login.html', context)

