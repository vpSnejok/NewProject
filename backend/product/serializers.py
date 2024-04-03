from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    cat_id = serializers.IntegerField()
