from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializers, CollectionSerializers
from django.db.models import Count

from django.shortcuts import get_object_or_404

# # Create your views here.
# """@api_view()
# def product_list(request):
#     # return HttpResponse("ok")
#     return Response("ok")"""


# # TODO creating Serializers

# """Serializer:(converts a model instace to a dictionary)
# - We need to convert product object to a JSON object
# - Serializer converts the product object to dict object
# - rest_framework have a jsocnrenderer class and this class have to render a method accept a dict object and returns json object."""

# # XXX issue if id =0 then show error
# # @api_view()
# # def product_detail(request, id):
# #     product = Product.objects.get(pk=id)
# #     serializer = ProductSerializers(product)
# #     return Response(serializer.data)


"""# solv:


# @api_view()
# def product_detail(request, id):
#     # method 1:
#     # try:
#     #     product = Product.objects.get(pk=id)
#     #     serializer = ProdcutSerializers(product)
#     #     return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     return Response(status=status.HTTP_400_BAD_REQUEST)

#     # method 2:
#     product = get_object_or_404(Product, pk=id)
#     serializer = ProductSerializers(product)
#     return Response(serializer.data)

#     #{
#     # "detail": "Not found."
#     # }
# """

# # TODO Deserializing Objects

# '''@api_view(["GET", "POST"])
# def product_list(request):
#     if request.method == "GET":
#         products = Product.objects.select_related("collection").all()
#         serializer = ProductSerializers(
#             products, many=True, context={"request": request}
#         )
#         return Response(serializer.data)
#     elif request.method == "POST":
#         # NOTE Deserializing Objects
#         serializer = ProductSerializers(data=request.data)
#         # NOTE Data Validation
#         # print(serializer.validated_data)
#         # ------------------
#         # method 1
#         # try:
#         #     if serializer.is_valid():
#         #         return Response("ok")
#         # except Exception:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # --------------
#         # method 2
#         # if serializer.is_valid(raise_exception=True):
#         #     return Response("ok")
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # --------------
#         # method 3 (recommanded)
#         serializer.is_valid(
#             raise_exception=True
#         )  # yee validate kar deta hai , but if we want extara validation like conform password
#         """
#         Product serailizer me yee function add karna hai
#          def validate(self, data):
#             if data['password']!=data['confirm_password']:
#                 return serializers.ValidationError("passwords not matched")
#             return data
#         """
#         # print(serializer.validated_data)
#         return Response("OK")

# '''


# # TODO save Objects


# @api_view(["GET", "POST"])
# def product_list(request):  # sourcery skip: remove-unreachable-code
#     if request.method == "GET":
#         products = Product.objects.select_related("collection").all()
#         serializer = ProductSerializers(
#             products, many=True, context={"request": request}
#         )
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = ProductSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#         """

#         There is some switchvation were we one override that how the product is created.

#         Isme humko kuch special filed set karna hota hai and user se differnet rup se lets hit wo

#         ProductSeraizers me 2 method add karna hoga
#         def create(self, validated_data):
#             product = Product(**validated_data)  # unpack the dict
#             product.other_field = 1
#             product.save()
#             return product

#         def update(self, instance, validated_data):
#             instance.unit_price = validated_data.get("unit_price")
#             instance.save()
#             return instance


#         """


# # NOTE [status code work](httpstatuses.com)
# @api_view(["GET", "PUT", "DELETE"])
# def product_detail(request, id):
#     product_obj = get_object_or_404(Product, pk=id)
#     if request.method == "GET":
#         serializer = ProductSerializers(product_obj)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ProductSerializers(product_obj, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == "DELETE":
#         if product_obj.orderitem_set.count() > 0:
#             return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product_obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def collection_list(request):
#     if request.method == "GET":
#         queryset = Collection.objects.annotate(product_count=Count("product")).all()
#         serialzer = CollectionSerializers(queryset, many=True)
#         return Response(serialzer.data)
#     elif request.method == "POST":
#         serialzer = CollectionSerializers(data=request.data)
#         serialzer.is_valid(raise_exception=True)
#         serialzer.save()
#         return Response(serialzer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(["GET", "PUT", "DELETE"])
# def collection_detail(request, pk):
#     collection = get_object_or_404(
#         Collection.objects.annotate(product_count=Count("product")), pk=pk
#     )
#     if request.method == "GET":
#         serializer = CollectionSerializers(collection)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = CollectionSerializers(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#     elif request.method == "DELETE":
#         if collection.product_set.count() > 0:
#             return Response({"error": "Collection cannot be deleted"})
#         collection.delete()
#         return Response("collection deleted", status=status.HTTP_204_NO_CONTENT)


# -----------------------------------

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializers, CollectionSerializers
from django.db.models import Count

from rest_framework.views import APIView

from rest_framework.views import APIView


class CollectionList(APIView):
    def get(self, request):
        queryset = Collection.objects.annotate(product_count=Count("product")).all()
        serialzer = CollectionSerializers(queryset, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = CollectionSerializers(data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        return Response(serialzer.data, status=status.HTTP_201_CREATED)


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.select_related("collection").all()
        serializer = ProductSerializers(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetails(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitem_set.count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionDetails(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(product_count=Count("product")), pk=pk
        )
        serializer = CollectionSerializers(collection)
        return Response(serializer.data)

    def put(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(product_count=Count("product")), pk=pk
        )
        serializer = CollectionSerializers(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(product_count=Count("product")), pk=pk
        )
        if collection.product_set.count() > 0:
            return Response({"error": "Collection cannot be deleted"})
        collection.delete()
        return Response("collection deleted", status=status.HTTP_204_NO_CONTENT)
