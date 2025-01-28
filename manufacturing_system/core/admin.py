from django.contrib import admin
from .models import Product, Supplier, Inventory, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_email', 'phone_number')
    search_fields = ('name', 'contact_email')
    list_filter = ('name',)
    ordering = ('name',)

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'restock_threshold')
    search_fields = ('product__name',)
    list_filter = ('quantity',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'customer_name', 'status', 'order_date')
    search_fields = ('product__name', 'customer_name', 'customer_email')
    list_filter = ('status', 'order_date')
    ordering = ('-order_date',)
