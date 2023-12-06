# pages/views.py

from django.shortcuts import render


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
    return render(request, 'pages/login.html', {})
