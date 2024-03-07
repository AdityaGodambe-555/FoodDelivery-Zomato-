from django.urls import path
from payapp import views

urlpatterns = [
    path('pay',views.pay),
    path('orderdet',views.order_det),
    path('orderview',views.order_view),
]
