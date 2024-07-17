from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ItemPagination(PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
        })