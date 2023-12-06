# pages/views.py

from django.shortcuts import render


# Create views here
def home(request):
    return render(request, "pages/home.html", {})
