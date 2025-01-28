# serializers.py
from rest_framework import serializers
from .models import Product, Supplier, Inventory, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_email', 'phone_number', 'address']

class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'product_name', 'quantity', 'restock_threshold']

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_name', 'quantity', 'customer_name', 'customer_email', 'order_date', 'status']

