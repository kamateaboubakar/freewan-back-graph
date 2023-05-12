import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .beverage_rack import queries as beverage_rack_queries
# beverage_rack_queries.BeverageRackQuery,

class BeverageRackQuery(graphene.ObjectType):
        
    BeverageRackNode = DjangoFilterConnectionField(types.BeverageRackType, filterset_class=types.BeverageRackFilter)
    def resolve_BeverageRackNode(self, info, **kwargs):
        pass
            
    BeverageRackBy_id = graphene.Field(types.BeverageRackType, id=graphene.ID(required=True))
    def resolve_BeverageRackBy_id(self, info, **kwargs):
        return models.BeverageRack.objects.get(**kwargs)
            