from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .gateways.types import GatewaysType, GatewaysFilter

class GatewaysFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Gateways
        fields = {field.name:['exact'] for field in models.Gateways._meta.fields}
    
        
class GatewaysType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Gateways
        filterset_class = GatewaysFilter
        interfaces = (graphene.relay.Node,)
            