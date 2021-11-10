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

from .forms import OrdersCreateViewDatePicker

#
from .models import Machine
from .models import Order
from .models import Product
from .models import Sensor

# Create your views here.
def wyswietl_strone_main(request ,*args, **kwargs):
	context = {
	}
	return render(request, "main.html", context)


def wyswietl_machines(request,*args, **kwargs):
	#wyświetla wszystkie machines i sidebar po lewej.
	context = { 'machines' : Machine.objects.all()
	}
	return render(request, "machines/machines.html", context)

class MachinesView(ListView):
	model = Machine
	template_name = 'machines/machines.html'
	context_object_name = 'machines'
	ordering = ['id']

class MachinesDetailView(DetailView):
	model = Machine
	template_name = 'machines/machine_details.html'
	context_object_name = 'machines'


class MachinesCreateView(LoginRequiredMixin,CreateView):
	model = Machine
	fields = ['name','description', 'performance']
	template_name = 'machines/add_machine.html'


class MachinesEditView(LoginRequiredMixin,UpdateView):
	model = Machine
	fields = ['name','description', 'performance']
	template_name = 'machines/edit_machine.html'

class MachinesDeleteView(LoginRequiredMixin,DeleteView):
	model = Machine
	template_name = 'machines/delete_machines.html'
	success_url = '/machines/'



class OrdersView(ListView):
	model = Order
	template_name = 'orders/orders.html'
	context_object_name = 'orders'
	ordering = ['id']

class OrdersDetailView(DetailView):
	model = Order
	template_name = 'orders/orders_details.html'
	context_object_name = 'orders'

class OrdersCreateView(LoginRequiredMixin,CreateView):
	model = Order
	form_class =  OrdersCreateViewDatePicker
	#fields = ['name','description', 'date_of_start','data_zakonczenia']
	template_name = 'orders/add_order.html'


class OrdersEditView(LoginRequiredMixin,UpdateView):
	model = Order
	fields = ['name','description', 'date_of_start','data_zakonczenia','visible']
	template_name = 'orders/edit_order.html'

class OrdersDeleteView(LoginRequiredMixin,DeleteView):
	model = Order
	template_name = 'machines/delete_order.html'
	success_url = 'orders/'


class ProductsView(LoginRequiredMixin,ListView):
	model = Product
	template_name = 'products/products.html'
	context_object_name = 'products'
	ordering = ['id']

class ProductsDetailView(LoginRequiredMixin,DetailView):
	model = Product
	template_name = 'products/product_details.html'
	context_object_name = 'products'


class ProductsCreateView(LoginRequiredMixin,CreateView):
	model = Product
	fields = ['name','description', 'item_mass']
	template_name = 'products/add_product.html'


class ProductsEditView(LoginRequiredMixin,UpdateView):
	model = Product
	fields = ['name','description', 'item_mass']
	template_name = 'products/edit_product.html'

class ProductsDeleteView(LoginRequiredMixin,DeleteView):
	model = Product
	template_name = 'machines/delete_product.html'
	success_url = '/products/'


class SensorView(LoginRequiredMixin,ListView):
	model = Sensor
	template_name = 'sensors/sensors.html'
	context_object_name = 'sensors'
	ordering = ['id']

class SensorDetailView(LoginRequiredMixin,DetailView):
	model = Sensor
	template_name = 'sensors/sensor_details.html'
	context_object_name = 'sensors'

class SensorCreateView(LoginRequiredMixin,CreateView):
	model = Sensor
	fields = ['name','description', 'przykladowy_odczyt','rodzaj_czujnika']#'rodzaje_czujnika_typy',
	template_name = 'sensors/add_sensor.html'


class SensorEditView(LoginRequiredMixin,UpdateView):
	model = Sensor
	fields = ['name','description', 'przykladowy_odczyt','rodzaj_czujnika']
	template_name = 'sensors/edit_sensor.html'

class SensorDeleteView(LoginRequiredMixin,DeleteView):
	model = Sensor
	template_name = 'sensors/delete_sensor.html'
	success_url = '/sensors/'


