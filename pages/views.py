# pages/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm


# Create views here
def home(request):
    return render(request, "pages/home.html", {})


def about(request):
    return render(request, 'pages/about.html', {})


def services(request):
    return render(request, 'pages/services.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})


def careers(request):
    return render(request, 'pages/careers.html', {})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')

    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


def blog(request):
    return render(request, 'pages/blog.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'pages/register.html', {'form', form})
