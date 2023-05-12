import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .region import queries as region_queries
# region_queries.RegionQuery,

class RegionQuery(graphene.ObjectType):
        
    RegionNode = DjangoFilterConnectionField(types.RegionType, filterset_class=types.RegionFilter)
    def resolve_RegionNode(self, info, **kwargs):
        pass
            
    RegionBy_id = graphene.Field(types.RegionType, id=graphene.ID(required=True))
    def resolve_RegionBy_id(self, info, **kwargs):
        return models.Region.objects.get(**kwargs)
            