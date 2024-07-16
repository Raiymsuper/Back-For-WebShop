from django_filters.rest_framework import FilterSet
import django_filters

from IaUstal import models


class ItemFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = models.Item
        fields = ['name']