from rest_framework.pagination import PageNumberPagination


class DafaultPagination(PageNumberPagination):
    page_size = 10
