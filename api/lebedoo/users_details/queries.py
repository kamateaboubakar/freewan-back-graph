import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .users_details import queries as users_details_queries
# users_details_queries.UsersDetailsQuery,

class UsersDetailsQuery(graphene.ObjectType):
        
    UsersDetailsNode = DjangoFilterConnectionField(types.UsersDetailsType, filterset_class=types.UsersDetailsFilter)
    def resolve_UsersDetailsNode(self, info, **kwargs):
        pass
            
    UsersDetailsBy_id = graphene.Field(types.UsersDetailsType, id=graphene.ID(required=True))
    def resolve_UsersDetailsBy_id(self, info, **kwargs):
        return models.UsersDetails.objects.get(**kwargs)
            