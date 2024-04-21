from django.contrib import admin
from.models import category,Product,Order


# Register your models here.
@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["category_name","description","created_at","updated_at"]
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","description","image","price"]
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=["customer_name","customer_email","quantity","product"]

