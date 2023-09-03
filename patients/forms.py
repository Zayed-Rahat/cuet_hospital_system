from django import forms
from .models import  PatientAccount

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientAccount
        fields = ['name', 'age', 'address', 'category']

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
        # Add custom form field configurations or widgets here if needed
