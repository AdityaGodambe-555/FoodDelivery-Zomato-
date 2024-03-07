from django.db import models

# Create your models here.
class Product(models.Model):
    CAT=((1,'Pizza'),(2,'Cake'),(3,'Chicken'),(4,'Snadwich'),(5,'Burger'))
    FTY=((1,'VEG'),(2,'NON-VEG'))
    name=models.CharField(max_length=50,verbose_name='Product Name')
    detail=models.CharField(max_length=500)
    price=models.FloatField()
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    f_type=models.IntegerField(verbose_name='Food Type',choices=FTY)
    product_image=models.ImageField(upload_to="productapp/image", default='')
    is_active=models.BooleanField(default=1,verbose_name='Status')
    
    
    