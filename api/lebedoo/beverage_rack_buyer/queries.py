import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .beverage_rack_buyer import queries as beverage_rack_buyer_queries
# beverage_rack_buyer_queries.BeverageRackBuyerQuery,

class BeverageRackBuyerQuery(graphene.ObjectType):
        
    BeverageRackBuyerNode = DjangoFilterConnectionField(types.BeverageRackBuyerType, filterset_class=types.BeverageRackBuyerFilter)
    def resolve_BeverageRackBuyerNode(self, info, **kwargs):
        pass
            
    BeverageRackBuyerBy_id = graphene.Field(types.BeverageRackBuyerType, id=graphene.ID(required=True))
    def resolve_BeverageRackBuyerBy_id(self, info, **kwargs):
        return models.BeverageRackBuyer.objects.get(**kwargs)
            