import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .years import queries as years_queries
# years_queries.YearsQuery,

class YearsQuery(graphene.ObjectType):
        
    YearsNode = DjangoFilterConnectionField(types.YearsType, filterset_class=types.YearsFilter)
    def resolve_YearsNode(self, info, **kwargs):
        pass
            
    YearsBy_id = graphene.Field(types.YearsType, id=graphene.ID(required=True))
    def resolve_YearsBy_id(self, info, **kwargs):
        return models.Years.objects.get(**kwargs)
            