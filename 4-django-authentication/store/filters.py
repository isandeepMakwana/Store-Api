from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            "collection_id": ["exact"],
            "unit_price": ["gt", "lt"],
        }


# By default, the search parameter is named 'search', but this may be overridden with the SEARCH_PARAM setting.

# To dynamically change search fields based on request content, it's possible to subclass the SearchFilter and override the get_search_fields() function. For example, the following subclass will only search on title if the query parameter title_only is in the request:

# from rest_framework import filters

# class CustomSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         if request.query_params.get('title_only'):
#             return ['title']
#         return super().get_search_fields(view, request)
