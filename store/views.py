from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.response import Http404
# Create your views here.


class ProductList(APIView):
    def get(self, request, format=None):
        products =  Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_slug):
        try:
            return Product.objects.get(slug = product_slug)
        except:
            raise Http404

    def get(self, request, product_slug, format=None):
        product = self.get_object(product_slug)
        serializer  = ProductSerializer(product)
        return Response(serializer.data)