from django.db import models
from cartapp.models import Cart
from productsapp.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    uid=models.ForeignKey(User, verbose_name=("Username"), on_delete=models.CASCADE, db_column='uid')
    order_id = models.CharField(max_length=150,verbose_name=("Order_Id"))
    count=models.IntegerField(verbose_name=("Count"))
    total=models.FloatField()
    paystat=models.BooleanField(default=0,verbose_name=("Payment"))
    
class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name=("Order_Id"))
    pid=models.ForeignKey(Product, verbose_name=("Product_Id"), on_delete=models.CASCADE, db_column='pid')
    quantity = models.IntegerField()


    