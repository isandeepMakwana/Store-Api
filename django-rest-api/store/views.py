from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProdcutSerializers

# Create your views here.
@api_view()
def product_list(request):
    # return HttpResponse("ok")
    return Response("ok")


# TODO creating Serializers

"""Serializer:(converts a model instace to a dictionary)
- We need to convert product object to a JSON object
- Serializer converts the product object to dict object
- rest_framework have a jsocnrenderer class and this class have to render a method accept a dict object and returns json object."""


@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProdcutSerializers(product)
    return Response(serializer.data)
