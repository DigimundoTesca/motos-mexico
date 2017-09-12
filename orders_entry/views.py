# import json
from django.shortcuts import render
from django.http import JsonResponse

from motorcycles.models import MotorcycleRegion
# Create your views here.


def home(request):
    template = 'index.html'
    context = {}
    if request.method == 'POST':
        return JsonResponse({'result': '1'})
    return render(request, template, context)


def new_order(request):
    if request.method == 'POST':
        print(request.POST)
    template = 'new_order.html'
    motrocycle_regions = MotorcycleRegion.objects.all()
    context = {
     'regions': motrocycle_regions
    }
    return render(request, template, context)
