from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .beverage_rack.types import BeverageRackType, BeverageRackFilter

class BeverageRackFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.BeverageRack
        fields = {field.name:['exact'] for field in models.BeverageRack._meta.fields}
    
        exclude = ['rack_details']
            
class BeverageRackType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.BeverageRack
        filterset_class = BeverageRackFilter
        interfaces = (graphene.relay.Node,)
            