from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .currencies.types import CurrenciesType, CurrenciesFilter

class CurrenciesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Currencies
        fields = {field.name:['exact'] for field in models.Currencies._meta.fields}
    
        
class CurrenciesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Currencies
        filterset_class = CurrenciesFilter
        interfaces = (graphene.relay.Node,)
            