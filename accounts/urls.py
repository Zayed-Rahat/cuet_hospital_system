from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.DoctorRegistrationView.as_view(), name='register'),
    path('login/', views.DoctorLoginView.as_view(), name='login'),
    path('logout/', views.DoctorLogoutView.as_view(), name='logout'),

]
