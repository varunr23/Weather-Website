from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('working/', views.working, name='working'),
]
