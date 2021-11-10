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
from produkcja.views import MachinesView, MachinesDetailView, MachinesCreateView, MachinesEditView, MachinesDeleteView
from produkcja.views import OrdersView, OrdersDetailView,  OrdersCreateView, OrdersEditView, OrdersDeleteView #OrdersCreateView_func as OrdersCreateView
from produkcja.views import ProductsView, ProductsDetailView, ProductsCreateView, ProductsEditView, ProductsDeleteView
from produkcja.views import SensorView, SensorDetailView, SensorCreateView, SensorEditView, SensorDeleteView


from users import views as users_views

urlpatterns = [
     path('', views.wyswietl_strone_main, name='main'),
     path('main', views.wyswietl_strone_main, name='main'),

     path('machines/', MachinesView.as_view(), name='machines'), 
     path('machines/<int:pk>/', MachinesDetailView.as_view(), name='machine_details'), 
     path('machines/new/', MachinesCreateView.as_view(), name='add_machine'), 
     path('machines/<int:pk>/edit/', MachinesEditView.as_view(), name='edit_machine'),
     path('machines/<int:pk>/delete/', MachinesDeleteView.as_view(), name='delete_machine'), 
     
     path('orders/', OrdersView.as_view(), name='orders'),
     path('orders/<int:pk>/', OrdersDetailView.as_view(), name='order_details'), 
     path('orders/new/', OrdersCreateView.as_view(), name='add_order'), 
     path('orders/<int:pk>/edit/', OrdersEditView.as_view(), name='edit_order'),
     path('orders/<int:pk>/delete/', OrdersDeleteView.as_view(), name='delete_order'), 

     path('products/', ProductsView.as_view(), name='products'),
     path('products/<int:pk>/', ProductsDetailView.as_view(), name='protuct_details'), 
     path('products/new/', ProductsCreateView.as_view(), name='add_product'), 
     path('products/<int:pk>/edit/', ProductsEditView.as_view(), name='edit_product'),
     path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='delete_product'), 

     path('sensors/', SensorView.as_view(), name='sensors'),
     path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor_details'), 
     path('sensors/new/', SensorCreateView.as_view(), name='add_sensor'), 
     path('sensors/<int:pk>/edit/', SensorEditView.as_view(), name='edit_sensor'),
     path('sensors/<int:pk>/delete/', SensorDeleteView.as_view(), name='delete_sensor'),


     #path('logowanie/', auth_views.LoginView.as_view(template_name = 'users/logowanie.html'), name='logowanie'), # gotowe templatey zajmujące się logowaniem i wylogowywaniem
     path('logowanie/', users_views.login, name='logowanie'), # gotowe templatey zajmujące się logowaniem i wylogowywaniem
     path('wylogowanie/', auth_views.LogoutView.as_view(template_name = 'users/wylogowanie.html'), name='wylogowanie'), # new
     path('rejestracja/', users_views.register, name='rejestracja'), # new
     path('profil/', users_views.profil_uzytkownika, name='profil'), # new


    path('admin/', admin.site.urls),

]
