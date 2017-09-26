# import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View

from motosmexico.reportpdf import render_pdf
from motorcycles.models import MotorcycleRegion, MotorcyclePart


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
    motorcycle_parts = MotorcyclePart.objects.all()
    context = {
     'regions': motrocycle_regions,
     'parts': motorcycle_parts,
    }
    return render(request, template, context)


class GeneratePDF(View):
    """
    Return PDF create to base to a template
    """
    def get(self, request, *args, **kwargs):
        context = {}
        pdf = render_pdf('report.html', context)
        return HttpResponse(pdf, content_type='application/pdf')