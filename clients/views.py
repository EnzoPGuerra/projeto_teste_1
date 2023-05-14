from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'clients/principal/home.html')

def Clients(request):
    
    return render(request, 'clients/principal/clients.html')