import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .country import queries as country_queries
# country_queries.CountryQuery,

class CountryQuery(graphene.ObjectType):
        
    CountryNode = DjangoFilterConnectionField(types.CountryType, filterset_class=types.CountryFilter)
    def resolve_CountryNode(self, info, **kwargs):
        pass
            
    CountryBy_id = graphene.Field(types.CountryType, id=graphene.ID(required=True))
    def resolve_CountryBy_id(self, info, **kwargs):
        return models.Country.objects.get(**kwargs)
            