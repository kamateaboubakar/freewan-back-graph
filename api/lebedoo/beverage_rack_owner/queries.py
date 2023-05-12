import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .beverage_rack_owner import queries as beverage_rack_owner_queries
# beverage_rack_owner_queries.BeverageRackOwnerQuery,

class BeverageRackOwnerQuery(graphene.ObjectType):
        
    BeverageRackOwnerNode = DjangoFilterConnectionField(types.BeverageRackOwnerType, filterset_class=types.BeverageRackOwnerFilter)
    def resolve_BeverageRackOwnerNode(self, info, **kwargs):
        pass
            
    BeverageRackOwnerBy_id = graphene.Field(types.BeverageRackOwnerType, id=graphene.ID(required=True))
    def resolve_BeverageRackOwnerBy_id(self, info, **kwargs):
        return models.BeverageRackOwner.objects.get(**kwargs)
            