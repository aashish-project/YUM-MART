from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User 

def user_directory_path(instense,filename):
    return 'media/user{0}/{1}'.format(instense.user.id,filename)



class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    picture=models.ImageField( upload_to=user_directory_path, max_length=None,verbose_name="profile-pic")
    first_name=models.CharField(max_length=50,name="first_name")
    last_name=models.CharField(max_length=50,name="second_name")
    dob=models.DateField(auto_now=False, auto_now_add=False)
    phone=PhoneNumberField()
    adress=models.TextField()
    # favourite=models.ManyToManyField(blank=True)

    def __str__(self):
        return self.user.username

class ShopKeeper(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    picture=models.ImageField( upload_to=user_directory_path, max_length=None,verbose_name="profile-pic")
    first_name=models.CharField(max_length=50,name="first_name")
    last_name=models.CharField(max_length=50,name="second_name")
    dob=models.DateField(auto_now=False, auto_now_add=False)
    phone=PhoneNumberField()
    adress=models.TextField()

    def __str__(self) -> str:
        return self.user.username