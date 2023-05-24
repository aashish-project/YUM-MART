from itertools import chain
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import *
from main.forms import Search
# Create your views here.
@login_required
def index(request):
    user=request.user
    items=Items.objects.all()
    favourites,is_created=Favourite.objects.get_or_create(user=user)
    # favourite_item=favourites[0].favourite.all().order_by('-date')[:10]
    tags=favourites.favourite.all()
    # print(favourite_item)
    items_set=set()
    for tag in tags:
        favourite_items=Items.objects.filter(category=tag)
        for fav in favourite_items:
            items_set.add(fav)
    # print(items_set)      
    mydict={}
    if request.method =='GET':
        form=Search(request.GET)
        if form.is_valid():
            mydict=form.search()
    else:
        form=Search()
    if 'restaurants' in mydict:
        restaurants = mydict['restaurants']
    else:
        restaurants=[]
    if 'titles' in mydict:
        titles = mydict['titles']
    else:
        titles=[]
    if 'descriptions' in mydict:
        descriptions = mydict['descriptions']
    else:
        descriptions=[]
    if 'categories' in mydict:
        categories = mydict['categories']
    else:
        categories=[]
    items_search = list(chain(restaurants, titles, descriptions, categories))

    context={
        'items':items,
        'tags':tags,
        'item_set':items_set,
        'items':items,
        "Restaurants":Restaurants.objects.all(),
        "form":form,
        'items':items_search,
    }
    # context.update(mydict)
    # print(items_search)

    return render(request,'home.html',context)

def buyItem(request,item_slug):
    item=Items.objects.get(item_slug=item_slug)
    
    pass