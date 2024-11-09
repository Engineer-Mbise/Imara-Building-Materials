from django.contrib import admin

# Register your models here.
from .models import Category,Product,Order


class OrderAdmin(admin.ModelAdmin):
    list_display=["customer_name","customer_phone_number","order_date","product","status","region","quantity"]


class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","description"]
    
class ProductAdmin(admin.ModelAdmin):
    list_display=["image","name","price","category"]
    search_fields = ("image","name","price","category")  # allow searching by name or category
    list_filter = ("image","name","price","category")
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)