from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import *
from .forms import Search

# Create your views here.

@login_required
def index(request,restaurents):
    context={}
    arr=[]
    
    user=request.user
    restaurants=get_object_or_404(Restaurants,name=restaurents)
    if(restaurants):
        menu=Menu.objects.filter(restaurants_name=restaurants)
    else:
        menu=Menu.objects.all()
    for i in menu:
        restaurants_name=i.restaurants_name.name
        restaurant_adress=i.restaurants_name.adress
        restaurant_contact=i.restaurants_name.contact
        items=i.item.all()
        arr.append([{'restaurants_name':restaurants_name},{'restaurant_adress':restaurant_adress},{'restaurant_contact':restaurant_contact},{'items':items}])


    form=Search()
    context={
        'data':arr,
        'form':form,
    }

    return render(request,'index.html',context)
def ItemFun(request,item_slug):
    item=Items.objects.get(item_slug=item_slug)
    context={
        'item':item,
        'rating':item.get_rating()
    }
    return render(request,'items-view.html',context)

def Main(request):
    if request.user in User.objects.all():
        return redirect('home')
    return redirect('login')