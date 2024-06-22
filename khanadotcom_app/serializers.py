from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "menu_item",
            "quantity",
            "price",
        )  # Adjust fields as per your OrderItem model


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source="orderitem_set", many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "order_id",
            "user",
            "delivery_address",
            "total_amount",
            "order_date",
            "items",
        )
