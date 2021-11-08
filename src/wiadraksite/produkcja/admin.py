from django.contrib import admin

# Register your models here.
from produkcja.models import Produkt, Maszyna, Czujnik, Polozenie_czujnika_w_maszynie,  Zlecenie, ilosc_elementow_ze_zlecenia, ilosc_elementow_ze_zlecenia_ma_przejsc_przez_maszyne
from produkcja.models import log_czujnika

admin.site.register(Produkt)
admin.site.register(Maszyna)
admin.site.register(Czujnik)
admin.site.register(Polozenie_czujnika_w_maszynie)
admin.site.register(log_czujnika)
admin.site.register(Zlecenie)
admin.site.register(ilosc_elementow_ze_zlecenia)
admin.site.register(ilosc_elementow_ze_zlecenia_ma_przejsc_przez_maszyne)