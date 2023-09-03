from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DoctorAccount
from django.contrib.auth.models import User


class DoctorRegistrationForm(UserCreationForm):
    specialties = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # form.save()
    def save(self, commit=True):
        our_user = super().save(commit=False) # ami database e data save korbo na ekhn
        if commit == True:
            our_user.save() # user model e data save korlam
            specialties = self.cleaned_data.get('specialties')
            
            DoctorAccount.objects.create(
                user = our_user,
                specialties =specialties,
                doctor_id = 1000+ our_user.id
            )
        return our_user    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })

