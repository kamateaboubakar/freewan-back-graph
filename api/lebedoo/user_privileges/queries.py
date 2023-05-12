import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .user_privileges import queries as user_privileges_queries
# user_privileges_queries.UserPrivilegesQuery,

class UserPrivilegesQuery(graphene.ObjectType):
        
    UserPrivilegesNode = DjangoFilterConnectionField(types.UserPrivilegesType, filterset_class=types.UserPrivilegesFilter)
    def resolve_UserPrivilegesNode(self, info, **kwargs):
        pass
            
    UserPrivilegesBy_id = graphene.Field(types.UserPrivilegesType, id=graphene.ID(required=True))
    def resolve_UserPrivilegesBy_id(self, info, **kwargs):
        return models.UserPrivileges.objects.get(**kwargs)
            