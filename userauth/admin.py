from django.contrib import admin

# Register your models here.
from userauth.models import Customer,ShopKeeper


admin.site.register(Customer)
admin.site.register(ShopKeeper)