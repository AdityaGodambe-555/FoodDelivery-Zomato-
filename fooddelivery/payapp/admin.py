from django.contrib import admin
from productsapp.models import Product
from payapp.models import Order
from payapp.models import OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=['uid','id','count','paystat']
    
class OrderItemAdmin(admin.ModelAdmin):
    def pid_display(self, obj):
        return obj.pid.name  
    pid_display.short_description = 'Product Name' 
    
    list_display=['order_id_id','pid_display','quantity']
    



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)