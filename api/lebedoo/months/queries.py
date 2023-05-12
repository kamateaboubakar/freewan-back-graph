import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .months import queries as months_queries
# months_queries.MonthsQuery,

class MonthsQuery(graphene.ObjectType):
        
    MonthsNode = DjangoFilterConnectionField(types.MonthsType, filterset_class=types.MonthsFilter)
    def resolve_MonthsNode(self, info, **kwargs):
        pass
            
    MonthsBy_id = graphene.Field(types.MonthsType, id=graphene.ID(required=True))
    def resolve_MonthsBy_id(self, info, **kwargs):
        return models.Months.objects.get(**kwargs)
            