import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .languages import queries as languages_queries
# languages_queries.LanguagesQuery,

class LanguagesQuery(graphene.ObjectType):
        
    LanguagesNode = DjangoFilterConnectionField(types.LanguagesType, filterset_class=types.LanguagesFilter)
    def resolve_LanguagesNode(self, info, **kwargs):
        pass
            
    LanguagesBy_id = graphene.Field(types.LanguagesType, id=graphene.ID(required=True))
    def resolve_LanguagesBy_id(self, info, **kwargs):
        return models.Languages.objects.get(**kwargs)
            