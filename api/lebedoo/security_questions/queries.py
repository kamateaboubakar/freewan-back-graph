import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .security_questions import queries as security_questions_queries
# security_questions_queries.SecurityQuestionsQuery,

class SecurityQuestionsQuery(graphene.ObjectType):
        
    SecurityQuestionsNode = DjangoFilterConnectionField(types.SecurityQuestionsType, filterset_class=types.SecurityQuestionsFilter)
    def resolve_SecurityQuestionsNode(self, info, **kwargs):
        pass
            
    SecurityQuestionsBy_id = graphene.Field(types.SecurityQuestionsType, id=graphene.ID(required=True))
    def resolve_SecurityQuestionsBy_id(self, info, **kwargs):
        return models.SecurityQuestions.objects.get(**kwargs)
            