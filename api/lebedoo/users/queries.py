import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .users import queries as users_queries
# users_queries.UsersQuery,

class UsersQuery(graphene.ObjectType):
        
    UsersNode = DjangoFilterConnectionField(types.UsersType, filterset_class=types.UsersFilter)
    def resolve_UsersNode(self, info, **kwargs):
        pass
            
    UsersBy_id = graphene.Field(types.UsersType, id=graphene.ID(required=True))
    def resolve_UsersBy_id(self, info, **kwargs):
        return models.Users.objects.get(**kwargs)
            