from rest_framework import pagination, status
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data={
            'message': 'Data retrieved successfully.',
            'data': {
                'current_page': self.page.number,
                'last_page': self.page.paginator.num_pages,
                'per_page': self.page.paginator.per_page,
                'total_data': self.page.paginator.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'results': data
            },
        }, status=status.HTTP_200_OK)
