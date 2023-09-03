from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import DoctorRegistrationForm
from django.contrib.auth import login, logout
from django.views.generic import FormView


class DoctorRegistrationView(FormView):
    template_name = 'doctor_signup.html'
    form_class = DoctorRegistrationForm
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    
class DoctorLoginView(LoginView):
    template_name = 'doctor_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class DoctorLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('login')



