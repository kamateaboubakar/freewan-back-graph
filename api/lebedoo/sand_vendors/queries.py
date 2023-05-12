import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .sand_vendors import queries as sand_vendors_queries
# sand_vendors_queries.SandVendorsQuery,

class SandVendorsQuery(graphene.ObjectType):
        
    SandVendorsNode = DjangoFilterConnectionField(types.SandVendorsType, filterset_class=types.SandVendorsFilter)
    def resolve_SandVendorsNode(self, info, **kwargs):
        pass
            
    SandVendorsBy_id = graphene.Field(types.SandVendorsType, id=graphene.ID(required=True))
    def resolve_SandVendorsBy_id(self, info, **kwargs):
        return models.SandVendors.objects.get(**kwargs)
            