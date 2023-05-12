from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .property_tenants.types import PropertyTenantsType, PropertyTenantsFilter

class PropertyTenantsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.PropertyTenants
        fields = {field.name:['exact'] for field in models.PropertyTenants._meta.fields}
    
        
class PropertyTenantsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.PropertyTenants
        filterset_class = PropertyTenantsFilter
        interfaces = (graphene.relay.Node,)
            