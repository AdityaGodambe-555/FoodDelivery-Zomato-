from django.db import models
from productsapp.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    uid=models.ForeignKey(User, verbose_name=("User_Id"), on_delete=models.CASCADE, db_column='uid')
    pid=models.ForeignKey(Product, verbose_name=("Product_Id"), on_delete=models.CASCADE, db_column='pid')
    qty=models.IntegerField(default=1, verbose_name=("Quantity"))