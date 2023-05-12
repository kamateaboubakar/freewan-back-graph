import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .gateways import queries as gateways_queries
# gateways_queries.GatewaysQuery,

class GatewaysQuery(graphene.ObjectType):
        
    GatewaysNode = DjangoFilterConnectionField(types.GatewaysType, filterset_class=types.GatewaysFilter)
    def resolve_GatewaysNode(self, info, **kwargs):
        pass
            
    GatewaysBy_id = graphene.Field(types.GatewaysType, id=graphene.ID(required=True))
    def resolve_GatewaysBy_id(self, info, **kwargs):
        return models.Gateways.objects.get(**kwargs)
            