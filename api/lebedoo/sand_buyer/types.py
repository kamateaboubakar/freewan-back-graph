from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .sand_buyer.types import SandBuyerType, SandBuyerFilter

class SandBuyerFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.SandBuyer
        fields = {field.name:['exact'] for field in models.SandBuyer._meta.fields}
    
        
class SandBuyerType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.SandBuyer
        filterset_class = SandBuyerFilter
        interfaces = (graphene.relay.Node,)
            