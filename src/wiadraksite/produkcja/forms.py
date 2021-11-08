from django import forms 
from django.views.generic import CreateView
from bootstrap_datepicker_plus import DatePickerInput
from .models import Zlecenie
from django.contrib.auth.mixins import LoginRequiredMixin

class ZleceniaCreateViewDatePicker(LoginRequiredMixin,CreateView):
	class Meta:
		model = Zlecenie
		fields = ['nazwa','opis', 'data_rozpoczecia','data_zakonczenia']
		widgets = {
            'data_rozpoczecia': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'data_zakonczenia': DatePickerInput(), 
        }	