from django.urls import path
from cartapp import views

urlpatterns = [
    path('',views.user_cart),
    path('addcart',views.add_cart),
    path('removeitem',views.remove_cart),
    path('updateqty',views.update_qty),
]
