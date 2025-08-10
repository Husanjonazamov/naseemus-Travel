from django_filters import rest_framework as filters

from core.apps.payment.models import PaymeModel


class PaymeFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PaymeModel
        fields = [
            "name",
        ]
