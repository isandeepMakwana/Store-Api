from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


# class ProductSerializers(serializers.Serializer):
#     """
#     serializer me models ki sarri field ho esa zaruri nhi hota. because of data base me kuch private data bhi hota hai or wo show nhi karna hota hai
#     """

#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2) #isme model ke field se match hai
#     price = serializers.DecimalField(
#         max_digits=6, decimal_places=2, source="unit_price"
#     )  # isme model ke field se match nhi hai

#     # TODO creating custom Serializer Fields
#     # API Model (interface) !=Data Model(implementation)
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

#     def calculate_tax(self, product):
#         return product.unit_price * Decimal(
#             1.1
#         )  # issue hota decimal not multiply to fload value

#     """
#     {
#         "id": 648,
#         "title": "7up Diet, 355 Ml",
#         "unit_price": 79.07,
#         "price_with_tax": 86.977
#     }
#     """
#     # and
#     """
#     {
#         "id": 648,
#         "title": "7up Diet, 355 Ml",
#         "price": 79.07,
#         "price_with_tax": 86.977
#     }
#     """


# TODO Seriallizing Relationships
"""


class CollectionSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    # NOTE primerykeyRelatedField
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    # NOTE StringRelatedField
    # collection = serializers.StringRelatedField()

    # NOTE inner object
    # collection = CollectionSerializers()

    # NOTE HyperlinkRelatedField
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name="collection-detail",
    )

    # create a url
    # path(r"collections/<int:id>/", views.collection_detail),

    # and makw a function in views like
    # def collectionl_detail(request, pk):
    #     ....
    #     ....
    #     ....

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(2.1)
"""

# TODO Model Serializers


class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "unit_price",
            "price_with_tax",
            "collection",
        ]

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name="collection-detail",
    # )
    price_with_tax = serializers.SerializerMethodField(method_name="calculated_tax")

    def calculated_tax(self, prodcut: Product):
        return prodcut.unit_price * Decimal(1.11)

    # def validate(self, data):
    #     if data['password']!=data['confirm_password']:
    #         return serializers.ValidationError("passwords not matched")
    #     return data
