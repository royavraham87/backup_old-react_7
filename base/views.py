from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
def index(req):
    return JsonResponse('hello', safe=False)


@api_view(['GET'])
def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return Response(all_products)