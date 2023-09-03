
from django.urls import path
from . import views
 
urlpatterns = [
    path('add_patient/', views.PatientCreateView.as_view(), name='add_patient'),
    path('patient_list/', views.PatientListView.as_view(), name='patient_list'),
    path('edit_patient/<int:pk>/', views.PatientUpdateView.as_view(), name='edit_patient'),
    path('delete_patient/<int:pk>/', views.PatientDeleteView.as_view(), name='delete_patient'),
    
]