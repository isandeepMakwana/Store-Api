from decimal import Decimal
from rest_framework import serializers


class ProdcutSerializers(serializers.Serializer):
    """
    serializer me models ki sarri field ho esa zaruri nhi hota. because of data base me kuch private data bhi hota hai or wo show nhi karna hota hai
    """

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2) isme model ke field se match hai
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )  # isme model ke field se match nhi hai

    # TODO creating custom Serializer Fields
    # NOTE API Model (interface) !=Data Model(implementation)
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product):
        return product.unit_price * Decimal(
            1.1
        )  # issue hota decimal not multiply to fload value

    """
    {
        "id": 648,
        "title": "7up Diet, 355 Ml",
        "unit_price": 79.07,
        "price_with_tax": 86.977
    }
    """
    # and
    """
    {
        "id": 648,
        "title": "7up Diet, 355 Ml",
        "price": 79.07,
        "price_with_tax": 86.977
    }
    """
