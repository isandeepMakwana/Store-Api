from django.urls import path
from . import views

urlpatterns = [
    # path(r"products/", views.product_list),
    # path(r"products/<int:id>/", views.product_detail),
    # path(r"collections/", views.collection_list),
    # path(r"collections/<int:pk>/", views.collection_detail, name="collection-detail"),
    path(r"products/", views.ProductList.as_view()),
    path(r"products/<int:id>/",views.ProductDetails.as_view()),
    path(r"collections/", views.CollectionList.as_view()),
    path(r"collection'/<int:id>/", views.CollectionDetails.as_view()),
]
