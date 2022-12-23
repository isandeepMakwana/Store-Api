from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

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
    "products", views.ProductViewSet
)  # r"products/" , r"products/<int:id>/"
router.register(
    "collections", views.CollectionViewSet
)  # r"collections/" , r"collections/<int:id>/"

# print(router.urls)

# urlpatterns = router.urls
urlpatterns = [path("", include(router.urls))]
