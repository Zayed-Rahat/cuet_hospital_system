from .forms import PatientForm
from django.urls import reverse_lazy
from .models import PatientAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = PatientAccount
    form_class = PatientForm
    template_name = 'add_patient.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        doctor = self.request.user.account
        form.instance.doctor = doctor
        return super().form_valid(form)


class PatientListView(LoginRequiredMixin, ListView):
    model = PatientAccount
    template_name = 'patient_list.html'
    context_object_name = 'patients'

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
