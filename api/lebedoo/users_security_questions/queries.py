import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .users_security_questions import queries as users_security_questions_queries
# users_security_questions_queries.UsersSecurityQuestionsQuery,

class UsersSecurityQuestionsQuery(graphene.ObjectType):
        
    UsersSecurityQuestionsNode = DjangoFilterConnectionField(types.UsersSecurityQuestionsType, filterset_class=types.UsersSecurityQuestionsFilter)
    def resolve_UsersSecurityQuestionsNode(self, info, **kwargs):
        pass
            
    UsersSecurityQuestionsBy_id = graphene.Field(types.UsersSecurityQuestionsType, id=graphene.ID(required=True))
    def resolve_UsersSecurityQuestionsBy_id(self, info, **kwargs):
        return models.UsersSecurityQuestions.objects.get(**kwargs)
            