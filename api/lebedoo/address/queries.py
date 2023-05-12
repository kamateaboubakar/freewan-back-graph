import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .address import queries as address_queries
# address_queries.AddressQuery,

class AddressQuery(graphene.ObjectType):
        
    AddressNode = DjangoFilterConnectionField(types.AddressType, filterset_class=types.AddressFilter)
    def resolve_AddressNode(self, info, **kwargs):
        pass
            
    AddressBy_id = graphene.Field(types.AddressType, id=graphene.ID(required=True))
    def resolve_AddressBy_id(self, info, **kwargs):
        return models.Address.objects.get(**kwargs)
            