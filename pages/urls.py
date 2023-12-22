from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('login/', views.custom_login, name='custom_login'),
    path('blog/', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('meet/', views.meet, name='meet')
]
