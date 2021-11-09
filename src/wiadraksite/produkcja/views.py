from django.shortcuts import render, redirect 
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin #to dodajesz zamiast dekoratorów typu login required
#from django.utils.timezone import now
#from django.utils.html import escape #służy do robienia Var dump. 
from django.contrib.auth import authenticate #służy do sprawdzenia czy użytkownik istnieje 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DatePickerInput
from django.views.generic.edit import FormView

from .forms import ZleceniaCreateViewDatePicker

#
from .models import Maszyna
from .models import Zlecenie
from .models import Produkt
from .models import Czujnik

# Create your views here.
def wyswietl_strone_glowna(request ,*args, **kwargs):
	context = {
	}
	return render(request, "glowna.html", context)


def wyswietl_maszyny(request,*args, **kwargs):
	#wyświetla wszystkie maszyny i sidebar po lewej.
	context = { 'maszyny' : Maszyna.objects.all()
	}
	return render(request, "maszyny/maszyny.html", context)

class MaszynyView(ListView):
	model = Maszyna
	template_name = 'maszyny/maszyny.html'
	context_object_name = 'maszyny'
	ordering = ['id']

class MaszynyDetailView(DetailView):
	model = Maszyna
	template_name = 'maszyny/detale_maszyny.html'
	context_object_name = 'maszyna'


class MaszynyCreateView(LoginRequiredMixin,CreateView):
	model = Maszyna
	fields = ['nazwa','opis', 'wydajnosc']
	template_name = 'maszyny/dodawanie_maszyny.html'


class MaszynyEditView(LoginRequiredMixin,UpdateView):
	model = Maszyna
	fields = ['nazwa','opis', 'wydajnosc']
	template_name = 'maszyny/edytowanie_maszyny.html'

class MaszynyDeleteView(LoginRequiredMixin,DeleteView):
	model = Maszyna
	template_name = 'maszyny/usuwanie_maszyny.html'
	success_url = '/maszyny/'



class ZleceniaView(ListView):
	model = Zlecenie
	template_name = 'zlecenia/zlecenia.html'
	context_object_name = 'zlecenia'
	ordering = ['id']

class ZleceniaDetailView(DetailView):
	model = Zlecenie
	template_name = 'zlecenia/detale_zlecenia.html'
	context_object_name = 'zlecenia'


# def ZleceniaCreateView_func(request):
#     if request.method == 'POST':
#     	form = ZleceniaCreateViewDatePicker(request.POST)
#     	if form.is_valid():
#    			wynik = form.save(request)
#    			if(wynik != None):
#    				return redirect('zlecenia/'+wynik)
#     else:
#    		form =  ZleceniaCreateViewDatePicker()
#     return render(request, 'zlecenia/dodawanie_zlecenia.html', {'form': form})



# class ZleceniaCreateViewCustom(LoginRequiredMixin,FormView):
# 	template_name = 'zlecenia/dodawanie_zlecenia.html'
# 	form_class = ZleceniaCreateViewDatePicker
# 	object_id = form_class.save()
# 	success_url = '/zlecenia' + object_id

class ZleceniaCreateView(LoginRequiredMixin,CreateView):
	model = Zlecenie
	form_class =  ZleceniaCreateViewDatePicker
	#fields = ['nazwa','opis', 'data_rozpoczecia','data_zakonczenia']
	template_name = 'zlecenia/dodawanie_zlecenia.html'


class ZleceniaEditView(LoginRequiredMixin,UpdateView):
	model = Zlecenie
	fields = ['nazwa','opis', 'data_rozpoczecia','data_zakonczenia','widoczne']
	template_name = 'zlecenia/edytowanie_zlecenia.html'

class ZleceniaDeleteView(LoginRequiredMixin,DeleteView):
	model = Zlecenie
	template_name = 'maszyny/usuwanie_zlecenia.html'
	success_url = 'zlecenia/'


class ProduktyView(LoginRequiredMixin,ListView):
	model = Produkt
	template_name = 'produkty/produkty.html'
	context_object_name = 'produkty'
	ordering = ['id']

class ProduktyDetailView(LoginRequiredMixin,DetailView):
	model = Produkt
	template_name = 'produkty/detale_produktu.html'
	context_object_name = 'produkty'


class ProduktyCreateView(LoginRequiredMixin,CreateView):
	model = Produkt
	fields = ['nazwa','opis', 'masa']
	template_name = 'produkty/dodawanie_produktu.html'


class ProduktyEditView(LoginRequiredMixin,UpdateView):
	model = Produkt
	fields = ['nazwa','opis', 'masa']
	template_name = 'produkty/edytowanie_produktu.html'

class ProduktyDeleteView(LoginRequiredMixin,DeleteView):
	model = Produkt
	template_name = 'maszyny/usuwanie_produktu.html'
	success_url = '/produkty/'


class CzujnikiView(LoginRequiredMixin,ListView):
	model = Czujnik
	template_name = 'czujniki/czujniki.html'
	context_object_name = 'czujniki'
	ordering = ['id']

class CzujnikiDetailView(LoginRequiredMixin,DetailView):
	model = Czujnik
	template_name = 'czujniki/detale_czujnika.html'
	context_object_name = 'czujniki'

class CzujnikiCreateView(LoginRequiredMixin,CreateView):
	model = Czujnik
	fields = ['nazwa','opis', 'przykladowy_odczyt','rodzaj_czujnika']#'rodzaje_czujnika_typy',
	template_name = 'czujniki/dodawanie_czujnika.html'


class CzujnikiEditView(LoginRequiredMixin,UpdateView):
	model = Czujnik
	fields = ['nazwa','opis', 'przykladowy_odczyt','rodzaj_czujnika']
	template_name = 'czujniki/edytowanie_czujnika.html'

class CzujnikiDeleteView(LoginRequiredMixin,DeleteView):
	model = Czujnik
	template_name = 'czujniki/usuwanie_czujnika.html'
	success_url = '/czujniki/'


