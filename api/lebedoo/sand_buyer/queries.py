import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .sand_buyer import queries as sand_buyer_queries
# sand_buyer_queries.SandBuyerQuery,

class SandBuyerQuery(graphene.ObjectType):
        
    SandBuyerNode = DjangoFilterConnectionField(types.SandBuyerType, filterset_class=types.SandBuyerFilter)
    def resolve_SandBuyerNode(self, info, **kwargs):
        pass
            
    SandBuyerBy_id = graphene.Field(types.SandBuyerType, id=graphene.ID(required=True))
    def resolve_SandBuyerBy_id(self, info, **kwargs):
        return models.SandBuyer.objects.get(**kwargs)
            