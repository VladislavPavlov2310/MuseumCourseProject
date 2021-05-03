from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('home')

    form = CreateUserForm()
    context = {
        'register_form': form
    }
    return render(request, 'user/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')

