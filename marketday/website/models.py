from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Market(models.Model):
	name = models.CharField(max_length=256, default='', blank=False)
	address = models.CharField(max_length=256, default='', blank=False)
	time = models.CharField(max_length=2048, default='', blank=True)
	location = models.CharField(max_length=256, default='', blank=False)



class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete =models.CASCADE)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)





   

    


	

    

    
    
    

    
   

    
    
    


  


