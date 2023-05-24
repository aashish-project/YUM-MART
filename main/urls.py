
from django.urls import path,include
from . import views
from django.contrib.auth import urls as auth_urls
urlpatterns = [
    path('<restaurents>',views.index,name='restaurents'),
    path('items/<item_slug>',views.ItemFun,name='items')
]
