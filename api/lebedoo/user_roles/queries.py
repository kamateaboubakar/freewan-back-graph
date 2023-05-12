import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .user_roles import queries as user_roles_queries
# user_roles_queries.UserRolesQuery,

class UserRolesQuery(graphene.ObjectType):
        
    UserRolesNode = DjangoFilterConnectionField(types.UserRolesType, filterset_class=types.UserRolesFilter)
    def resolve_UserRolesNode(self, info, **kwargs):
        pass
            
    UserRolesBy_id = graphene.Field(types.UserRolesType, id=graphene.ID(required=True))
    def resolve_UserRolesBy_id(self, info, **kwargs):
        return models.UserRoles.objects.get(**kwargs)
            