import django_filters
from .models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    price = django_filters.NumberFilter(field_name='price')

    class Meta:
        model = Item
        fields = ['name', 'price']
