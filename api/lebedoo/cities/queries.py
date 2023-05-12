import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .cities import queries as cities_queries
# cities_queries.CitiesQuery,

class CitiesQuery(graphene.ObjectType):
        
    CitiesNode = DjangoFilterConnectionField(types.CitiesType, filterset_class=types.CitiesFilter)
    def resolve_CitiesNode(self, info, **kwargs):
        pass
            
    CitiesBy_id = graphene.Field(types.CitiesType, id=graphene.ID(required=True))
    def resolve_CitiesBy_id(self, info, **kwargs):
        return models.Cities.objects.get(**kwargs)
            