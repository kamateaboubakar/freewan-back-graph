import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .currencies import queries as currencies_queries
# currencies_queries.CurrenciesQuery,

class CurrenciesQuery(graphene.ObjectType):
        
    CurrenciesNode = DjangoFilterConnectionField(types.CurrenciesType, filterset_class=types.CurrenciesFilter)
    def resolve_CurrenciesNode(self, info, **kwargs):
        pass
            
    CurrenciesBy_id = graphene.Field(types.CurrenciesType, id=graphene.ID(required=True))
    def resolve_CurrenciesBy_id(self, info, **kwargs):
        return models.Currencies.objects.get(**kwargs)
            