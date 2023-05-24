from django.shortcuts import render,redirect
from django.http import HttpResponse 
from main.models import Items
from .models import *
from main.models import Favourite
from django.db import transaction
# Create your views here.

def BuyItems(request,item_slug): #this add to the favourite
    try:
        user=request.user
        items=Items.objects.get(item_slug=item_slug)
        favourite,is_created=Favourite.objects.get_or_create(user=user)
        for resto in items.restaurant.all():
            favourite.restaurants.add(resto)
        for tag in items.category.all():
            favourite.favourite.add(tag)
        # print(favourite.favourite.all)
        favourite.save()
        return True
    except Exception as e:

        return False

def buy(request,item_slug): #this add to the cart
    try:
        item=Items.objects.get(item_slug=item_slug)
        cart_user,is_created=Cart.objects.get_or_create(user=request.user)
        cart_user.items.add(item)
        cart_user.save()
        check=BuyItems(request,item_slug)
        print(check) #there are printing statements
        if check==True:
            check=True
        else:
            check=False
        print(check)
        return redirect('home')
    except Exception as e:
        print(e)
        return HttpResponse(e)



def ShowCart(request):
    user=request.user
    if(Cart.objects.exists()):
        cart=Cart.objects.get(user=user)
    else:
        return HttpResponse("Cart is empty")
    items=cart.items.all()
    total_price=cart.get_price()
    context={
        'item':items,
        'total_price':total_price,
    }
    return render(request,'cart/items.html',context)
def Remove_Item_Cart(request,item_slug):
    cart=Cart.objects.get(user=request.user)
    item=cart.items.get(item_slug=item_slug)
    cart.items.remove(item)
    cart.save()
    return redirect('show_cart')

def PurchasedFun(request,item_slug,order_complete=False):
    item=Items.objects.get(item_slug=item_slug)
    # item_Purchased,is_created=Item_Purchased.objects.get_or_create(item=item)
    # purchased.delivery_person=User.objects.get(username='vikas')
    purchased,is_created=Purchased.objects.get_or_create(user=request.user,delivery_person=User.objects.get(username='vikas'))
    purchased.item.add(item)
    purchased.save()
    print(purchased.item.all())
    if order_complete:
        with transaction.atomic():
            purchased.orderComplete(item=item)
    context={
        'purchased_item':purchased.item.all()
    }
    return render(request,'buy/items.html',context)