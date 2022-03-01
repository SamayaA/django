from attr import field
from rest_framework import serializers

from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ["id", "title", "description"]


# Serializer for product position in stock
class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta():
        model = StockProduct
        fields = ["id", "product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta():
        model = Stock
        fields = ["id", "address", "positions"]

    def create(self, validated_data):
        # related data of other tables
        positions = validated_data.pop('positions')
        # create stock with given data params
        stock = super().create(validated_data)
        #saving data
        for position in positions:
            pos = StockProduct(
                stock=stock,
                product=position["product"],
                quantity=position["quantity"],
                price=position["price"],
            )
            pos.save()

        return stock

    def update(self, instance, validated_data):
        # related data of other tables
        positions = validated_data.pop('positions')
        # update stock params
        stock = super().update(instance, validated_data)
        # update related table
        for position in positions:
            instance.positions.product = position["product"]
            instance.positions.quantity = position["quantity"]
            instance.positions.price = position["price"]
        return stock
