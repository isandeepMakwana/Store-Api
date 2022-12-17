from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("get_objects/", views.get_product_data),
    path("filtering_objects/", views.Filtering_Objects),
    path("more_operations/", views.function_for_more),
    path("pre_load/", views.pre_load),
    path("sql_functions/", views.sql_functions),
    path("Querying_Generic_Relationships/", views.Querying_Generic_Relationships),
    path("understanding_QuerySet_Cache/", views.understanding_QuerySet_Cache),
    path("curd/", views.CRUD_opreations),
    path("executing_Raw_SQL_Queries/", views.executing_Raw_SQL_Queries),
]
