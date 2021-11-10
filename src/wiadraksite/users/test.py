So. This is my working custom login form. 
The problem starts when i type wrong password :P 

from .forms import CustomUserLoginForm
def login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            form.save(request) #ta funkcja loguje weryfikuje i loguje użytkownika
            username = form.cleaned_data.get('username')
            messages.success(request, f'Witaj {username}!')
            return redirect('main')
        #else:
            #username = form.cleaned_data.get('username')
            #messages.fail(request, f'Nie udało się zalogować użytkownika {username}!')
            #return redirect('logowanie')
    else:
        form = CustomUserLoginForm() 
    return render(request, 'users/logowanie.html',{'form':form})

  and Class

from django.contrib.auth import authenticate, login as auth_login
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
            raise  ValidationError("Wrong password/Złe hasło") #Here is the problem. 
        return user


How to make it to display ValidationError at the form url? 
The error ive get 
Exception Type:     ValidationError
Exception Value: ['Wrong password/Złe hasło']
Exception Location:   .... forms.py, in save