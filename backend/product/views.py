# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
#
# from product.models import Product
# from product.serializers import ProductSerializer
#
#
# # Create your views here.
#
# class ProductAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        p = Product.objects.all()
        return Response({'posts': ProductSerializer(p, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Product.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': ProductSerializer(post_new).data})
