from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from userauth.models import ShopKeeper
# Create your models here.


def user_directory_path(instense,filename):
    return 'user{0}/{1}'.format(instense.user.id,filename)

class Category(models.Model):
    tag=models.CharField(max_length=50,verbose_name="tag",name="tag")
    slug=models.SlugField(null=False,editable=False,unique=True,default=uuid.uuid1)
    class Meta:
        verbose_name="Tag"
        verbose_name_plural="Tags"

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse(user_directory_path, args=[self.slug])
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.slug)
        return super().save(*args, **kwargs)
    
class Review(models.Model):
    user=models.ManyToManyField(User,name='user')
    rating=models.IntegerField()
    body=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.body+' | '+str(self.rating)


class Restaurants(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    adress=models.CharField(max_length=200,null=False,blank=False)
    contact=PhoneNumberField()
    email=models.EmailField(max_length=254,name='email',null=False,blank=False)
    
    class Meta:
        verbose_name="Restaurant"
        verbose_name_plural="Restaurants"

    def __str__(self):
        return self.name
    
class Items(models.Model):
    user=models.ForeignKey(ShopKeeper,on_delete=models.CASCADE,null=True)
    # user=User.objects.get(username='aashish')
    restaurant=models.ManyToManyField(Restaurants, related_name="restaurant")
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=500)
    category=models.ManyToManyField(Category,related_name='category')
    reviews=models.ManyToManyField(Review,related_name='review')
    price=models.IntegerField(null=False)
    item_slug=models.SlugField(null=False,editable=True,unique=True,default=uuid.uuid1)
    picture=models.ImageField(upload_to=user_directory_path,blank=False,null=False,verbose_name='item_picture')
    discount=models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse("items", args=[str(self.item_slug)] )

    # def get_absolute_url(self):
    #     return reverse("post-detail", args=[str(self.id)] )
    def get_rating(self):
        reviews=self.reviews.all()
        if reviews:
            total_rating=sum(review.rating for review in reviews)
            return total_rating/len(reviews)
        return 0
    class Meta:
        verbose_name='Item'
        verbose_name_plural="Items"
    
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Menu(models.Model):
    restaurants_name=models.OneToOneField(Restaurants, on_delete=models.CASCADE,related_name='restaurants')
    item=models.ManyToManyField(Items , related_name="items")

    def __str__(self):
        return self.restaurants_name.name
    def rating(self)->int:
        rating=0
        if self.category.__len__() !=0:
            for i in self.category:
                rating+=i.rating
            return rating/self.category.__len__()
        return rating

class Delivery(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='delivery')
    contact=PhoneNumberField()
    def __str__(self):
        return self.user.username

class Favourite(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    favourite=models.ManyToManyField(Category, related_name='favourite',blank=True)
    restaurants=models.ManyToManyField(Restaurants,related_name='Favourite_restaurants',blank=True)
    date=models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
    class Meta:
        verbose_name="Favourite"
        verbose_name_plural="Favourite"
    