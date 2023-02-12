from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers


# Routers
# router = SimpleRouter()
router = DefaultRouter()
router.register(
    "products",
    views.ProductViewSet,  # basename="product"
)  # r"products/" , r"products/<int:id>/"
router.register(
    "collections",
    views.CollectionViewSet,  # basename="collection"
)  # r"collections/" , r"collections/<int:id>/"
router.register("carts", views.CartViewSet, basename="cart")


# print(router.urls)

# TODO nested routers
# [https://github.com/alanjds/drf-nested-routers](https://github.com/alanjds/drf-nested-routers)


products_nested_router = routers.NestedDefaultRouter(
    router, r"products", lookup="products"
)
products_nested_router.register(
    r"reviews", views.ReviewsViewSet, basename="products-reviews"
)


cart_nested_router = routers.NestedDefaultRouter(
    router, r"carts", lookup="carts"  # yee indirectly carts__{pk} hota hia
)
cart_nested_router.register(
    r"cartitems", views.CartItemViewSet, basename="carts-cartitems"
)


# urlpatterns = router.urls+product_nested_router.urls+cart_nested_router.urls
urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(products_nested_router.urls)),
    path(r"", include(cart_nested_router.urls)),
]


# router = DefaultRouter()
# router.register(r'products', views.ProductViewSet, basename='products')

# urlpatterns = [
#     path('products/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
# ]
