from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)  # the url can be blank also no needd compulsory

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) #here photos can upload in the profile_pic folder in media directory


    def __str__(self):
        return self.user.username


class south_breakfast(models.Model):
    name=models.CharField(max_length=15)
    image=models.ImageField(upload_to='media/media/pics')
    rupees=models.IntegerField()

class south_lunch(models.Model):
    name=models.CharField(max_length=15)
    image=models.ImageField(upload_to='media/media/pics')
    rupees=models.IntegerField()

class south_dinner(models.Model):
    name=models.CharField(max_length=15)
    image=models.ImageField(upload_to='media/media/pics')
    rupees=models.IntegerField()

class north_breakfast(models.Model):
     name=models.CharField(max_length=15)
     image=models.ImageField(upload_to='media/media/pics')
     rupees=models.IntegerField()

class north_lunch(models.Model):
     name=models.CharField(max_length=15)
     image=models.ImageField(upload_to='media/media/pics')
     rupees=models.IntegerField()

class north_dinner(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='media/media/pics')
    rupees=models.IntegerField()

class orders(models.Model):
    Address=models.CharField(max_length=40)
    street_name=models.CharField(max_length=40)
    phone_no=models.CharField(max_length=20)
    customer_name=models.CharField(max_length=40,default='true',blank='true')
