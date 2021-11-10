from django import forms 
from django.contrib.auth.models import User #tu importuję bazodanowy model użytkownika. 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.core.exceptions import ValidationError #Tego użyję w Customowej funkcji tworzenia użytkownika



class UserRegisterForm(UserCreationForm): #tak odbywa się dziedziczenie
	email=forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Wpisz login', min_length=4, max_length=150)
    email = forms.EmailField(label='Wpisz E-mail')
    password1 = forms.CharField(label='Wpisz hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Ten użytkownik już istnieje")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Ten email został już użyty")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasła muszą być takie same")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


#z tym formularzem to jest niezła jazda:
# def login(request):
#     if request.method == 'POST':
#         form = CustomUserLoginForm(request.POST)
#         if form.is_valid():
#             form.save(request) #ta funkcja po prostu zapisuje do bazy danych nowego użytkownika
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Witaj {username}!')
#             return redirect('main')
#     else:
#         form = CustomUserLoginForm(request.POST)
#     return render(request, 'users/logowanie.html',{'form':form})

class CustomUserLoginForm(forms.Form):
    username = forms.CharField(label='Wpisz login', min_length=4, max_length=150)
    password = forms.CharField(label='Wpisz hasło', widget=forms.PasswordInput)
    
    def clean_login(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(login=username)
        if r.count() == 0:
            raise  ValidationError("Wrong password/Złe hasło")
        return username
   
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

    def save(self, request):
        user = authenticate(
            username = self.cleaned_data['username'], 
            password = self.cleaned_data['password']
            )
        if user is not None:
        	auth_login(request, user)
        else:
            return None
        	#raise  ValidationError("Wrong password/Złe hasło")
        return user



# class CustomLoginForm(AuthenticationForm):
#     username = forms.CharField(label='Wpisz login', min_length=4, max_length=150)
#     password = forms.CharField(label='Wpisz hasło', widget=forms.PasswordInput)