from django.contrib import admin


from main.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Restaurants)
admin.site.register(Menu)
admin.site.register(Delivery)
admin.site.register(Items)