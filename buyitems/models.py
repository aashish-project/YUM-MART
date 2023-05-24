from django.db import models
from django.contrib.auth.models import User
from main.models import Items,Favourite
# Create your models here.
class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='cart_user')
    items=models.ManyToManyField(Items,related_name='cart_items')
    class Meta:
        verbose_name='Cart'
        verbose_name_plural="Cart"
    
    def get_price(self):
        price=sum([item.price for item in self.items.all()])
        return price
    def __str__(self) -> str:
        return self.user.username
    
    # def save(self,*args, **kwargs):
    #     items=self.items.all
    #     favourite=Favourite.objects.get_or_create(user=self.user)
    #     for item in items:
    #         categorys=item.category.all
    #         for category in categorys:
    #             favourite.category.add(category)
    #     favourite.save()
    #     return super().save(*args, **kwargs)

    
class Purchased(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="purchased_user")
    item=models.ManyToManyField(Items,related_name="purchased_Item",blank=True)
    delivery_person=models.OneToOneField(User,on_delete=models.CASCADE,name="delivery_person")
    
    def __str__(self) -> str:
        return self.user.username

    def orderComplete(self,item)->bool:
        # try:
            purchased=Purchased.objects.get(user=self.user)
            purchased.item.remove(item)
            purchased.save()
            return True
        # except:
        #     return False
    