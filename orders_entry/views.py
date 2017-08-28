from django.shortcuts import render

# Create your views here.


def home(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def new_order(request):
    if request.method == 'POST':
        print(request.POST)
    template = 'new_order.html'
    context = {}
    return render(request, template, context)
