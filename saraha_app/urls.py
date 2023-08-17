"""saraha_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import *
from django.conf.urls.static import static
from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('interface/<str:user_identifier>/', views.interface, name='interface'),
    path('index/<str:user_identifier>/<str:uuid>/', views.index, name='index'),
    path('comments/<str:user_identifier>/<str:uuid>/', views.comments, name='comments'),
    path('contact/', views.contact, name='contact'),
    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('reply/<str:user_identifier>/<str:uuid>/', views.reply, name='reply'),  # Missing comma was added here
    path('success/<str:user_identifier>/<str:uuid>/', views.success, name='success'),
]
    