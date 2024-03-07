from django.contrib import admin
from productsapp.models import Product
# Register your models here.

admin.site.site_header = 'Zomato ADMIN PAGE'
admin.site.site_title = ' Admin'
admin.site.index_title = 'Welcome To Zomato Admin'


class ProductAdmin(admin.ModelAdmin):
    list_filter=['cat','is_active','f_type']
    list_display=['name','detail','price','cat','f_type']

admin.site.register(Product,ProductAdmin)