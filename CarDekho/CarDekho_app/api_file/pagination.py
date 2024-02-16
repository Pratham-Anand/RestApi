from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class ReviewlistPagination(PageNumberPagination):
    page_size=1

class Reviewlistlimitoffpag(LimitOffsetPagination):
    default_limit=1