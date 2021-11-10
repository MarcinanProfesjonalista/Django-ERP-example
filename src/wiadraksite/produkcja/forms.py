from django import forms 
from django.views.generic import CreateView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin

# class DateInput(forms.DateInput):
#     input_type = 'date'

class OrdersCreateViewDatePicker(forms.ModelForm):
	date_of_start = forms.DateField(required = False,label="Data rozpoczęcia zlecenia", widget=forms.TextInput(     
        attrs={'type': 'date'} 
    ))
	data_zakonczenia = forms.DateField(required = False,label="Data zakończenia zlecenia", widget=forms.TextInput(   
        attrs={'type': 'date'} 
    ))
	class Meta:
			model = Order
			fields = ['name','description','date_of_start','data_zakonczenia']




