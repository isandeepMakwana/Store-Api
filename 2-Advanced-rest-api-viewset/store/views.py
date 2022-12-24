from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from .models import Product, Collection, OrderItem, Reviews
from .filters import ProductFilter
from .serializers import ProductSerializers, CollectionSerializers, ReviewsSerializers


# TODO ViewSets

# productList , productDetails in one class
"""class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("collection").all()
    serializer_class = ProductSerializers

    def get_serializer_context(self):
        return {"request": self.request}

    # delete method for delete all list and one object also
    def destroy(self, request, *args, **kwargs):  # delete one objects
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count():
            return Response({"error": "Product cannot be deleted."})
        return super().destroy(request, *args, **kwargs)"""


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(product_count=Count("product")).all()
    serializer_class = CollectionSerializers

    # delete method for delete all list and one object also
    # def destroy(self, request, pk):
    #     collection = get_object_or_404(Collection, pk=pk)
    #     if collection.product_set.count() > 0:
    #         return Response({"error": "Product cannot be deleted."})
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response({"error": "Product cannot be deleted."})
        return super().destroy(request, *args, **kwargs)


# TODO Building the Reviews API

"localhost:8000/store/products/1/reviews/"
"localhost:8000/store/products/1/reviews/1/"

# - create a model class
# - create a migrations
# -apply the migrations

# - create a serializer
# - create a view
# - register a route


class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

    def get_queryset(self):
        return Reviews.objects.filter(product_id=self.kwargs["products_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["products_pk"]}


# TODO filtering

"localhost:8000/store/products?collections_id=1"


"""class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.select_related("collection").all()
    serializer_class = ProductSerializers

    def get_queryset(self):
        queryset = Product.objects.all()
        collection_id = self.request.query_params.get("collection_id")
        # you can add more
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id).all()
        return queryset

    def get_serializer_context(self):
        return {"request": self.request}

    # delete method for delete all list and one object also
    def destroy(self, request, *args, **kwargs):  # delete one objects
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count():
            return Response({"error": "Product cannot be deleted."})
        return super().destroy(request, *args, **kwargs)
"""

# TODO Genric Filtering
# pip install django-filters
# and inside of installed_app ['django_filters',....]
"http://localhost:8000/store/products/?collection_id=3&unit_price=36"
"http://localhost:8000/store/products/?unit_price=36"


"""class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["collection_id", "unit_price"]

    def get_serializer_context(self):
        return {"request": self.request}

    # delete method for delete all list and one object also
    def destroy(self, request, *args, **kwargs):  # delete one objects
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count():
            return Response({"error": "Product cannot be deleted."})
        return super().destroy(request, *args, **kwargs)"""


# NOTE now i want to build unit_price < 100 and unit_price >30
# [django filters]()
#  - create a file <filters.py>
"http://localhost:8000/store/products/?collection_id=3&unit_price__gt=10&unit_price__lt=20"


"""class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_serializer_context(self):
        return {"request": self.request}

    # delete method for delete all list and one object also
    def destroy(self, request, *args, **kwargs):  # delete one objects
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count():
            return Response({"error": "Product cannot be deleted."})
        return super().destroy(request, *args, **kwargs)"""


# TODO Searching
"http://localhost:8000/store/products/?search=apple"
"http://localhost:8000/store/products/?search=apple+10xz"

# '^' Starts-with search.
# '=' Exact matches.
# '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
# '$' Regex search.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = [
        "^title",
        "description",
        # "collection__title",
    ]  # collection_title is not showing but it search internaly

    ## change the search to find
    # http://localhost:8000/store/products/?find=Anchovy
    """    REST_FRAMEWORK = {
        "COERCE_DECIMAL_TO_STRING": False,
        "SEARCH_PARAM": "find",
    }"""

    def get_serializer_context(self):
        return {"request": self.request}

    # delete method for delete all list and one object also
    def destroy(self, request, *args, **kwargs):  # delete one objects
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count():
            return Response({"error": "Product cannot be deleted."})
        return super().destroy(request, *args, **kwargs)


# TODO Sorting
