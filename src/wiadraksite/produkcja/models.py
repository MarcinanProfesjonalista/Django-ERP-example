from django.db import models
from datetime import datetime 
from django.utils.timezone import now
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa produktu")
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis produktu")
    item_mass = models.DecimalField(max_digits = 10, decimal_places = 0, null=True, blank=True, verbose_name="Masa produktu")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('product_details',kwargs={'pk':self.pk})


class Machine(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa machines")
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis machines")
    performance = models.CharField(max_length=100, null=True, blank=True, verbose_name="Wydajność machines")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('machine_details',kwargs={'pk':self.pk})

class Sensor(models.Model):
    name = models.CharField(max_length=50,default="Sensor", verbose_name="Nazwa czujnika")
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis czujnika")
    rodzaje_czujnikow = (
        ('ciagly', 'Licznik(pomiar ciągły)'),
        ('chwilowy', 'Termometr(pomiar chwilowy)'),
        ('masy_ciagly', 'Waga(pomiar sumowany)'),
        ('masy_chwilowy', 'Waga(pomiar chwilowy)')
    )
    rodzaj_czujnika = models.CharField(choices=rodzaje_czujnikow, max_length=50, verbose_name="Rodzaj czujnika") 
    przykladowy_odczyt = models.DecimalField(max_digits = 6, decimal_places = 2, null=True, blank=True, verbose_name="Przykładowa wartość odczytu")
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('detale_czujnika',kwargs={'pk':self.pk})

class Location_sensor_in_machine(models.Model):
	id_Sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	id_Machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
	polozenie_czujnika_rodzaje = (
        ('wejscia', 'Sensor na wejściu machines'),
        ('wewnetrzny', 'Sensor oprzyrządowania machines'),
        ('wyjsca', 'Sensor na wyjściu machines'),
    )
	sensor_placement = models.CharField(choices=polozenie_czujnika_rodzaje, max_length=50, verbose_name="Położenie czujnika w maszynie")
	prefix =  models.CharField(max_length=50, null=True, blank=True,verbose_name="Prefix wartości")
	suffix =  models.CharField(max_length=50, null=True, blank=True,verbose_name="Suffix wartości")


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa zlecenia")
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis zlecenia")
    date_of_start = models.DateField(null=True, blank=True, verbose_name="Data rozpoczęcia zlecenia")
    data_zakonczenia = models.DateField(null=True, blank=True, verbose_name="Data zakończenia zlecenia")
    visible = models.BooleanField(default=True, verbose_name='Czy zlecenie jest visible?')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('order_details',kwargs={'pk':self.pk})

class number_of_elements_from_the_order(models.Model):
    id_Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_elements= models.DecimalField(max_digits = 6, decimal_places = 0)
    

class the_number_of_elements_from_the_order_to_pass_through_the_machine(models.Model):
    id_zlecenia = models.ForeignKey(number_of_elements_from_the_order, on_delete=models.CASCADE)
    id_machines = models.ForeignKey(Machine, on_delete=models.CASCADE)
    time_per_element = models.DurationField(null=True, blank=True, verbose_name='Czas na jeden element?')

class sensor_log(models.Model):
	id_czujnika = models.CharField(max_length=10)
	created =models.DateTimeField(default=now) #models.DateTimeField(auto_now=True, default=datetime.now()) #timestamp udejta
	wartosc_zmierzona = models.CharField(max_length=10)
	
