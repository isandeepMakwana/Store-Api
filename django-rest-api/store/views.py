from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProdcutSerializers

from django.shortcuts import get_object_or_404

# Create your views here.
"""@api_view()
def product_list(request):
    # return HttpResponse("ok")
    return Response("ok")"""


# TODO creating Serializers

"""Serializer:(converts a model instace to a dictionary)
- We need to convert product object to a JSON object
- Serializer converts the product object to dict object
- rest_framework have a jsocnrenderer class and this class have to render a method accept a dict object and returns json object."""

# XXX issue if id =0 then show error
# @api_view()
# def product_detail(request, id):
#     product = Product.objects.get(pk=id)
#     serializer = ProdcutSerializers(product)
#     return Response(serializer.data)

# solv:


@api_view()
def product_detail(request, id):
    # method 1:
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProdcutSerializers(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    # method 2:
    product = get_object_or_404(Product, pk=id)
    serializer = ProdcutSerializers(product)
    return Response(serializer.data)

    """{
    "detail": "Not found."
    }"""


@api_view()
def product_list(request):
    products = Product.objects.all()
    serializer = ProdcutSerializers(products, many=True)
    return Response(serializer.data)
