
from django.urls import path
from .views import placement_statistics

urlpatterns = [
    path('placement_statistics/', placement_statistics, name='placement_statistics'),
]