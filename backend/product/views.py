from django.shortcuts import render
from rest_framework.generics import ListAPIView

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
