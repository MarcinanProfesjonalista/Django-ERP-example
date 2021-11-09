from django import forms 
from django.views.generic import CreateView
from .models import Zlecenie
from django.contrib.auth.mixins import LoginRequiredMixin

# class DateInput(forms.DateInput):
#     input_type = 'date'

class ZleceniaCreateViewDatePicker(forms.ModelForm):
	data_rozpoczecia = forms.DateField(required = False,label="Data rozpoczęcia zlecenia", widget=forms.TextInput(     
        attrs={'type': 'date'} 
    ))
	data_zakonczenia = forms.DateField(required = False,label="Data zakończenia zlecenia", widget=forms.TextInput(   
        attrs={'type': 'date'} 
    ))
	class Meta:
			model = Zlecenie
			fields = ['nazwa','opis','data_rozpoczecia','data_zakonczenia']




