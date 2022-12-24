from decimal import Decimal
from store.models import Product, Collection, Reviews

from rest_framework import serializers


class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "product_count"]

    product_count = serializers.IntegerField(required=False)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "inventory",
            "unit_price",
            "price_with_tax",
            "collection",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculated_tax")

    def calculated_tax(self, product: Product):
        return product.unit_price * Decimal(1.11)


class ReviewsSerializers(serializers.ModelSerializer):

    product = serializers.SerializerMethodField(method_name="get_product")

    class Meta:
        model = Reviews
        fields = [
            "id",
            "date",
            "name",
            "description",
            "product",
        ]

    def get_product(self, review):
        return review.product_id

    def create(self, validated_data):
        product_id = self.context["product_id"]
        # print("====>",product_id)
        return Reviews.objects.create(product_id=product_id, **validated_data)
