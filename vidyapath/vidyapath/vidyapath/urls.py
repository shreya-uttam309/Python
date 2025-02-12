"""
URL configuration for vidyapath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from .views import notice

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),  # URL for register.html
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('notice/', views.notice, name='notice'),
    path('notice/update_notice/<int:id>/', views.update_notice, name='update_notice'),
    path('notice/update_notice/update_notice1/<int:id>/', views.update_notice1, name='update_notice1'),
    path("notice/delete1/<int:id>/", views.delete1, name="delete1"),
    path("admindashboard/delete/<int:id>/", views.delete, name="delete"),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('placement/', views.placement, name='placement'),
    path('learningdev/', views.learningdev, name='learningdev'),
    path('placementg/', views.placementg, name='placementg'),
    path('login/', views.login, name='login'),
    #path("update_notice/<int:notice_id>/", update_notice, name="update_notice"),
] 