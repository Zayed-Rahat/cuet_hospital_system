from django.db import models
# from category.models import Category
from accounts.models import DoctorAccount

class PatientAccount(models.Model):
    doctor = models.ForeignKey(DoctorAccount, related_name = 'patient', on_delete=models.CASCADE)    
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=[('Heart', 'Heart Patients'), ('Liver', 'Liver Patients')])
    def __str__(self):
        return self.name
