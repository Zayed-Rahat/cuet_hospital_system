from django.shortcuts import render
from django.views.generic import ListView
from patients.models import PatientAccount
# Create your views here.

class HomeView(ListView):
    model = PatientAccount
    template_name = 'index.html'
    context_object_name = 'patients'
