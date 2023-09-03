from django.db import models
from django.contrib.auth.models import User

# django amaderke built in user niye kaj korar facility dey


class DoctorAccount(models.Model):
    user = models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    doctor_id = models.IntegerField(unique=True)

    specialties = models.CharField(max_length=10)

    
    def __str__(self):
        return str(self.doctor_id)


