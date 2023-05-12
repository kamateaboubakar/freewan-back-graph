from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .address.types import AddressType, AddressFilter

class AddressFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Address
        fields = {field.name:['exact'] for field in models.Address._meta.fields}
    
        
class AddressType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Address
        filterset_class = AddressFilter
        interfaces = (graphene.relay.Node,)
            