from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .beverage_rack_owner.types import BeverageRackOwnerType, BeverageRackOwnerFilter

class BeverageRackOwnerFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.BeverageRackOwner
        fields = {field.name:['exact'] for field in models.BeverageRackOwner._meta.fields}
    
        
class BeverageRackOwnerType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.BeverageRackOwner
        filterset_class = BeverageRackOwnerFilter
        interfaces = (graphene.relay.Node,)
            