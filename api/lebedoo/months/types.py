from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .months.types import MonthsType, MonthsFilter

class MonthsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Months
        fields = {field.name:['exact'] for field in models.Months._meta.fields}
    
        
class MonthsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Months
        filterset_class = MonthsFilter
        interfaces = (graphene.relay.Node,)
            