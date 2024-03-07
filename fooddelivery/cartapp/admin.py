from django.contrib import admin
from cartapp.models import Cart
from productsapp.models import Product

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    def pid_display(self, obj):
        return obj.pid.name  
    pid_display.short_description = 'Product Name'  
    
    list_filter = ['uid']
    list_display = ['uid', 'pid_display', 'qty']


admin.site.register(Cart, CartAdmin)