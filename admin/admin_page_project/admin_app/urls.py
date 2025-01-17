from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('frontend-home/', views.frontend_home, name='home1'),
    path('add-student/', views.add_student, name='add_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('view-notices/', views.view_notices, name='view_notices'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('register/', views.register, name='register'),
    path('insertuser/', views.insertuser, name='insertuser'),
]