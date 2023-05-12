from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .sand_vendors.types import SandVendorsType, SandVendorsFilter

class SandVendorsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.SandVendors
        fields = {field.name:['exact'] for field in models.SandVendors._meta.fields}
    
        
class SandVendorsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.SandVendors
        filterset_class = SandVendorsFilter
        interfaces = (graphene.relay.Node,)
            