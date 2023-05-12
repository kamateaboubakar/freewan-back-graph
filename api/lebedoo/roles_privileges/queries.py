import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .roles_privileges import queries as roles_privileges_queries
# roles_privileges_queries.RolesPrivilegesQuery,

class RolesPrivilegesQuery(graphene.ObjectType):
        
    RolesPrivilegesNode = DjangoFilterConnectionField(types.RolesPrivilegesType, filterset_class=types.RolesPrivilegesFilter)
    def resolve_RolesPrivilegesNode(self, info, **kwargs):
        pass
            
    RolesPrivilegesBy_id = graphene.Field(types.RolesPrivilegesType, id=graphene.ID(required=True))
    def resolve_RolesPrivilegesBy_id(self, info, **kwargs):
        return models.RolesPrivileges.objects.get(**kwargs)
            