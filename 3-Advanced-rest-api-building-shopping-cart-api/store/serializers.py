from decimal import Decimal
from store.models import Product, Collection, Reviews, Cart, CartItem

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


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "unit_price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name="get_total_price")

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, source="cartitem_set", read_only=True)
    total_price = serializers.SerializerMethodField(method_name="get_final_total")

    def get_final_total(self, cart: Cart):
        return sum(
            item.quantity * item.product.unit_price for item in cart.cartitem_set.all()
        )

    class Meta:
        model = Cart
        fields = ["id", "created_at", "items", "total_price"]



