from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers


# urlpatterns = [
#     path(r"products/", views.ProductList.as_view()),
#     path(r"products/<int:id>/",views.ProductDetails.as_view()),
#     path(r"collections/", views.CollectionList.as_view()),
#     path(r"collection'/<int:id>/", views.CollectionDetails.as_view()),
# ]


# Routers
# router = SimpleRouter()
router = DefaultRouter()
router.register(
    "products", views.ProductViewSet, basename="product"
)  # r"products/" , r"products/<int:id>/"
router.register(
    "collections", views.CollectionViewSet, basename="collection"
)  # r"collections/" , r"collections/<int:id>/"

# print(router.urls)

# TODO nested routers
# [https://github.com/alanjds/drf-nested-routers](https://github.com/alanjds/drf-nested-routers)


products_nested_router = routers.NestedSimpleRouter(
    router, r"products", lookup="products"
)
products_nested_router.register(
    r"reviews", views.ReviewsViewSet, basename="products-reviews"
)


# urlpatterns = router.urls+product_nested_router.urls
urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(products_nested_router.urls)),
]
