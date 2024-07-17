from django_filters import rest_framework as filters
from .models import Item


class ItemFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
    price = filters.NumberFilter()

    class Meta:
        model = Item
        fields = ['name', 'price']