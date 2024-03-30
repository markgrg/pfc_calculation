from django.shortcuts import render

def index(request):
    return render(request, 'pfc_calculator/index.html')

def about(request):
    return render(request, 'pfc_calculator/about.html')
