from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializers, CollectionSerializers

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
@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)


"""# solv:


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
    serializer = ProductSerializers(product)
    return Response(serializer.data)

    #{
    # "detail": "Not found."
    # }
"""

# TODO Deserializing Objects


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.select_related("collection").all()
        serializer = ProductSerializers(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data)
    elif request.method == "POST":
        # NOTE Deserializing Objects
        serializer = ProductSerializers(data=request.data)
        # NOTE Data Validation
        # print(serializer.validated_data)
        # ------------------
        # method 1
        # try:
        #     if serializer.is_valid():
        #         return Response("ok")
        # except Exception:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # --------------
        # method 2
        # if serializer.is_valid(raise_exception=True):
        #     return Response("ok")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # --------------
        # method 3 (recommanded)
        serializer.is_valid(
            raise_exception=True
        )  # yee validate kar deta hai , but if we want extara validation like conform password
        """
        Product serailizer me yee function add karna hai
         def validate(self, data):
            if data['password']!=data['confirm_password']:
                return serializers.ValidationError("passwords not matched")
            return data
        """
        # print(serializer.validated_data)
        return Response("OK")


@api_view()
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializers(collection)
    return Response(serializer.data)


# TODO save Objects

