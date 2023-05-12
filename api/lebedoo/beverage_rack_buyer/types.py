from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .beverage_rack_buyer.types import BeverageRackBuyerType, BeverageRackBuyerFilter

class BeverageRackBuyerFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.BeverageRackBuyer
        fields = {field.name:['exact'] for field in models.BeverageRackBuyer._meta.fields}
    
        
class BeverageRackBuyerType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.BeverageRackBuyer
        filterset_class = BeverageRackBuyerFilter
        interfaces = (graphene.relay.Node,)
            