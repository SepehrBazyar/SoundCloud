from rest_framework.pagination import (
    PageNumberPagination,
)


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "size"
    page_query_param = "page"
