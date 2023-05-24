from django.urls import path,include
from home import views
from buyitems import views as b_views  

urlpatterns = [
    path("",views.index,name="home"),
    path("buy/<item_slug>",b_views.PurchasedFun , name="buy"),
    path("order/<item_slug>/<order_complete>",b_views.PurchasedFun , name="buy"),
]
