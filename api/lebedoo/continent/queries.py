import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .continent import queries as continent_queries
# continent_queries.ContinentQuery,

class ContinentQuery(graphene.ObjectType):
        
    ContinentNode = DjangoFilterConnectionField(types.ContinentType, filterset_class=types.ContinentFilter)
    def resolve_ContinentNode(self, info, **kwargs):
        pass
            
    ContinentBy_id = graphene.Field(types.ContinentType, id=graphene.ID(required=True))
    def resolve_ContinentBy_id(self, info, **kwargs):
        return models.Continent.objects.get(**kwargs)
            