from django.db import models
from django.contrib.auth.models import User


#będę rozszerzał model user o profil. Będzie to relacja 1 - 1. 
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imie_nazwisko = models.CharField(max_length = 50, null=True, blank=True)
	#image = models.ImageField(default='default.jpg', upload_to='profile_pics') #to żąda ode mnie instalacji dodatku pillow do obsługi zdjęć. Nie warto wg. mnie. 

	def __str__(self):
		return f'{self.user.username} Profile'

