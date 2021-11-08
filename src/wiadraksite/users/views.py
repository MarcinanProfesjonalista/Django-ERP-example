from django.shortcuts import render, redirect #redirect aby przekierować po sukcesie
#to wywalasz po odziedziczeniu #from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages #tu wyświetlasz coś na podbe vardump. message.debug message.info .. success .warning .error

#from .forms import UserRegisterForm  #tu importujesz z form.py oddziedziczony form z UserCreationForm
from .forms import CustomUserCreationForm
from .forms import CustomUserLoginForm

from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save() #ta funkcja po prostu zapisuje do bazy danych nowego użytkownika
			username = form.cleaned_data.get('username')
			messages.success(request, f'Stworzono nowego użytkownika dla konta {username}!')
			return redirect('logowanie')
	else:
		form = CustomUserCreationForm()
	return render(request, 'users/rejestracja.html',{'form':form})


def login(request):
	if request.method == 'POST':
		form = CustomUserLoginForm(request.POST)
		if form.is_valid():
			if(form.save(request) != None): #ta funkcja loguje weryfikuje i loguje użytkownika
				username = form.cleaned_data.get('username')
				messages.success(request, f'Witaj {username}!')
				return redirect('glowna')
			else: 
				username = form.cleaned_data.get('username')
				messages.warning(request, f'Nie udało się zalogować użytkownika {username}!')
				return render(request, 'users/logowanie.html',{'form':form})
	else:
		form = CustomUserLoginForm() 
	return render(request, 'users/logowanie.html',{'form':form})


@login_required #tu dodałem dekorator który żąda zalogowowania aby móc zajrzeć do tego miejsca. 
def profil_uzytkownika(request):
	return render(request,'users/profil.html')