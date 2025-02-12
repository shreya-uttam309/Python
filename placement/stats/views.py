from django.shortcuts import render
from .models import PlacementStatistic

def placement_statistics(request):
    statistics = PlacementStatistic.objects.all().order_by('-year')
    return render(request, 'placement_statistics.html', {'statistics': statistics})