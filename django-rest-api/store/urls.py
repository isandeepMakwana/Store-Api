from django.urls import path
from . import views

urlpatterns = [
    path(r"products/", views.product_list),
    path(r"products/<int:id>/", views.product_detail),
]