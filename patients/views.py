from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from .forms import  PatientForm 
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.views import View
from django.shortcuts import redirect
from .models import PatientAccount
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView




class PatientCreateView(LoginRequiredMixin, CreateView):
    model = PatientAccount
    form_class = PatientForm
    template_name = 'add_patient.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        doctor = self.request.user.account
        form.instance.doctor = doctor
        return super().form_valid(form)    
    

class PatientListView(LoginRequiredMixin,ListView):
    model = PatientAccount
    template_name = 'patient_list.html'
    context_object_name = 'patients'
    ordering = ['category', 'name']  # Sort patients by category in descending order, then by name

    def get_queryset(self):
        category_filter = self.request.GET.get('category_filter')
        queryset = super().get_queryset()
        # Filter patients by the current logged-in doctor
        queryset = queryset.filter(doctor=self.request.user.account)
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset

    

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = PatientAccount
    form_class = PatientForm
    template_name = 'add_patient.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = PatientAccount
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('patient_list')