from attr import field
from rest_framework import serializers

from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta():
        model = StockProduct
        fields = ["id", "product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta():
        model = Stock
        fields = ["address", "positions"]

    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        
        # заполнение связанной таблицы
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
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # обновим связанные таблицы
        for position in positions:
            instance.positions.product = position["product"]
            instance.positions.quantity = position["quantity"]
            instance.positions.price = position["price"]
            
        return stock
