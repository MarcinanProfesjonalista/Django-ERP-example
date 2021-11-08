from django.db import models
from datetime import datetime 
from django.utils.timezone import now
from django.urls import reverse
# Create your models here.


class Produkt(models.Model):
    nazwa = models.CharField(max_length=50, verbose_name="Nazwa produktu")
    opis = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis produktu")
    masa = models.DecimalField(max_digits = 10, decimal_places = 0, null=True, blank=True, verbose_name="Masa produktu")

    def __str__(self):
        return self.nazwa
    def get_absolute_url(self):
        return reverse ('detale_produktu',kwargs={'pk':self.pk})


class Maszyna(models.Model):
    nazwa = models.CharField(max_length=50, verbose_name="Nazwa maszyny")
    opis = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis maszyny")
    wydajnosc = models.CharField(max_length=100, null=True, blank=True, verbose_name="Wydajność maszyny")

    def __str__(self):
        return self.nazwa
    def get_absolute_url(self):
        return reverse ('detale_maszyny',kwargs={'pk':self.pk})

class Czujnik(models.Model):
    nazwa = models.CharField(max_length=50, verbose_name="Nazwa czujnika")
    opis = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis czujnika")
    rodzaje_czujnika_typy = models.TextChoices('rodzaj_czujnika', 'Licznik(Pomiar ciągły), Termometr(Pomiar chwilowy)')
    przykladowy_odczyt = models.DecimalField(max_digits = 6, decimal_places = 2, null=True, blank=True, verbose_name="Przykładowa wartość odczytu")

    def __str__(self):
        return self.nazwa
    def get_absolute_url(self):
        return reverse ('detale_czujnika',kwargs={'pk':self.pk})

class Polozenie_czujnika_w_maszynie(models.Model):
	id_czujnika = models.ForeignKey(Czujnik, on_delete=models.CASCADE)
	id_maszyny = models.ForeignKey(Maszyna, on_delete=models.CASCADE)
	polozenie_czujnika_rodzaje = (
        ('wejscia', 'Czujnik na wejściu maszyny'),
        ('wewnetrzny', 'Czujnik oprzyrządowania maszyny'),
        ('wyjsca', 'Czujnik na wyjściu maszyny'),
    )
	polozenie_czujnika = models.CharField(choices=polozenie_czujnika_rodzaje, max_length=10, verbose_name="Położenie czujnika w maszynie")
	prefix =  models.CharField(max_length=50, null=True, blank=True,verbose_name="Prefix wartości")
	suffix =  models.CharField(max_length=50, null=True, blank=True,verbose_name="Suffix wartości")


class Zlecenie(models.Model):
    nazwa = models.CharField(max_length=50, verbose_name="Nazwa zlecenia")
    opis = models.CharField(max_length=50, null=True, blank=True, verbose_name="Opis zlecenia")
    data_rozpoczecia = models.DateField(null=True, blank=True, verbose_name="Data rozpoczęcia zlecenia")
    data_zakonczenia = models.DateField(null=True, blank=True, verbose_name="Data zakończenia zlecenia")
    widoczne = models.BooleanField(default=True, verbose_name='Czy zlecenie jest widoczne?')

    def __str__(self):
        return self.nazwa
    def get_absolute_url(self):
        return reverse ('detale_zlecenia',kwargs={'pk':self.pk})

class ilosc_elementow_ze_zlecenia(models.Model):
    id_zlecenia = models.ForeignKey(Zlecenie, on_delete=models.CASCADE)
    id_elementu = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc_elementow= models.DecimalField(max_digits = 6, decimal_places = 0)
    

class ilosc_elementow_ze_zlecenia_ma_przejsc_przez_maszyne(models.Model):
    id_zlecenia = models.ForeignKey(ilosc_elementow_ze_zlecenia, on_delete=models.CASCADE)
    id_maszyny = models.ForeignKey(Maszyna, on_delete=models.CASCADE)
    time_per_element = models.DurationField(null=True, blank=True, verbose_name='Czas na jeden element?')

class log_czujnika(models.Model):
	id_czujnika = models.CharField(max_length=10)
	created =models.DateTimeField(default=now) #models.DateTimeField(auto_now=True, default=datetime.now()) #timestamp udejta
	wartosc_zmierzona = models.CharField(max_length=10)
	
