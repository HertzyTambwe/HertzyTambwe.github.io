from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'portfolio/index.html')

def my_projets(request):
    
    return render(request, 'portfolio/projets.html')