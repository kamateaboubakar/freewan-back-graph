from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .property_owners.types import PropertyOwnersType, PropertyOwnersFilter

class PropertyOwnersFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.PropertyOwners
        fields = {field.name:['exact'] for field in models.PropertyOwners._meta.fields}
    
        
class PropertyOwnersType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.PropertyOwners
        filterset_class = PropertyOwnersFilter
        interfaces = (graphene.relay.Node,)
            