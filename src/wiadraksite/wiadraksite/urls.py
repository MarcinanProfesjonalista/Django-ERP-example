"""wiadraksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from produkcja import views
from produkcja.views import MaszynyView, MaszynyDetailView, MaszynyCreateView, MaszynyEditView, MaszynyDeleteView
from produkcja.views import ZleceniaView, ZleceniaDetailView, ZleceniaCreateView, ZleceniaEditView, ZleceniaDeleteView
from produkcja.views import ProduktyView, ProduktyDetailView, ProduktyCreateView, ProduktyEditView, ProduktyDeleteView
from produkcja.views import CzujnikiView, CzujnikiDetailView, CzujnikiCreateView, CzujnikiEditView, CzujnikiDeleteView


from users import views as users_views

urlpatterns = [
     path('', views.wyswietl_strone_glowna, name='glowna'),
     path('glowna', views.wyswietl_strone_glowna, name='glowna'),
     path('maszyny/', MaszynyView.as_view(), name='maszyny'), 
     path('maszyny/<int:pk>/', MaszynyDetailView.as_view(), name='detale_maszyny'), 
     path('maszyny/new/', MaszynyCreateView.as_view(), name='dodawanie_maszyny'), 
     path('maszyny/<int:pk>/edit/', MaszynyEditView.as_view(), name='edytowanie_maszyny'),
     path('maszyny/<int:pk>/delete/', MaszynyDeleteView.as_view(), name='usuwanie_maszyny'), 
     
     path('zlecenia/', ZleceniaView.as_view(), name='zlecenia'),
     path('zlecenia/<int:pk>/', ZleceniaDetailView.as_view(), name='detale_zlecenia'), 
     path('zlecenia/new/', ZleceniaCreateView.as_view(), name='dodawanie_zlecenia'), 
     path('zlecenia/<int:pk>/edit/', ZleceniaEditView.as_view(), name='edytowanie_zlecenia'),
     path('zlecenia/<int:pk>/delete/', ZleceniaDeleteView.as_view(), name='usuwanie_zlecenia'), 

     path('produkty/', ProduktyView.as_view(), name='produkty'),
     path('produkty/<int:pk>/', ProduktyDetailView.as_view(), name='detale_produktu'), 
     path('produkty/new/', ProduktyCreateView.as_view(), name='dodawanie_produktu'), 
     path('produkty/<int:pk>/edit/', ProduktyEditView.as_view(), name='edytowanie_produktu'),
     path('produkty/<int:pk>/delete/', ProduktyDeleteView.as_view(), name='usuwanie_produktu'), 

     path('czujniki/', CzujnikiView.as_view(), name='czujniki'),
     path('czujniki/<int:pk>/', CzujnikiDetailView.as_view(), name='detale_czujnika'), 
     path('czujniki/new/', CzujnikiCreateView.as_view(), name='dodawanie_czujnika'), 
     path('czujniki/<int:pk>/edit/', CzujnikiEditView.as_view(), name='edytowanie_czujnika'),
     path('czujniki/<int:pk>/delete/', CzujnikiDeleteView.as_view(), name='usuwanie_czujnika'),


     #path('logowanie/', auth_views.LoginView.as_view(template_name = 'users/logowanie.html'), name='logowanie'), # gotowe szablony zajmujące się logowaniem i wylogowywaniem
     path('logowanie/', users_views.login, name='logowanie'), # gotowe szablony zajmujące się logowaniem i wylogowywaniem
     path('wylogowanie/', auth_views.LogoutView.as_view(template_name = 'users/wylogowanie.html'), name='wylogowanie'), # new
     path('rejestracja/', users_views.register, name='rejestracja'), # new
     path('profil/', users_views.profil_uzytkownika, name='profil'), # new


    path('admin/', admin.site.urls),

]
