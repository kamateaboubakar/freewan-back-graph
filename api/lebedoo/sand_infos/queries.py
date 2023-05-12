import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .sand_infos import queries as sand_infos_queries
# sand_infos_queries.SandInfosQuery,

class SandInfosQuery(graphene.ObjectType):
        
    SandInfosNode = DjangoFilterConnectionField(types.SandInfosType, filterset_class=types.SandInfosFilter)
    def resolve_SandInfosNode(self, info, **kwargs):
        pass
            
    SandInfosBy_id = graphene.Field(types.SandInfosType, id=graphene.ID(required=True))
    def resolve_SandInfosBy_id(self, info, **kwargs):
        return models.SandInfos.objects.get(**kwargs)
            