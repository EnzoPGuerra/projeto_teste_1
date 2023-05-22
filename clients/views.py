from django.shortcuts import render
from django.views.generic import ListView, FormView
from . import models
# Create your views here.

def Home(request):
    return render(request, 'clients/principal/home.html')


class Clients(ListView):
    model = models.Clients
    template_name = 'clients/principal/clients.html'
    context_object_name = 'clients'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        qs.order_by('-id')
        return qs

        

