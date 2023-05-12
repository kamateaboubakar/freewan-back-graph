import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .municipalities import queries as municipalities_queries
# municipalities_queries.MunicipalitiesQuery,

class MunicipalitiesQuery(graphene.ObjectType):
        
    MunicipalitiesNode = DjangoFilterConnectionField(types.MunicipalitiesType, filterset_class=types.MunicipalitiesFilter)
    def resolve_MunicipalitiesNode(self, info, **kwargs):
        pass
            
    MunicipalitiesBy_id = graphene.Field(types.MunicipalitiesType, id=graphene.ID(required=True))
    def resolve_MunicipalitiesBy_id(self, info, **kwargs):
        return models.Municipalities.objects.get(**kwargs)
            