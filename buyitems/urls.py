from django.urls import path
from buyitems.views import *
from django.urls import reverse
# url=reverse('buyitems:')

urlpatterns = [
    path('',ShowCart,name='show_cart'),
    path('remove-from-cart/<item_slug>',Remove_Item_Cart,name='remove_from_cart'),
    path('add-to-cart/<item_slug>',buy,name="add_cart")
]