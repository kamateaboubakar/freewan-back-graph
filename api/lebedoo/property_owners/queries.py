import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .property_owners import queries as property_owners_queries
# property_owners_queries.PropertyOwnersQuery,

class PropertyOwnersQuery(graphene.ObjectType):
        
    PropertyOwnersNode = DjangoFilterConnectionField(types.PropertyOwnersType, filterset_class=types.PropertyOwnersFilter)
    def resolve_PropertyOwnersNode(self, info, **kwargs):
        pass
            
    PropertyOwnersBy_id = graphene.Field(types.PropertyOwnersType, id=graphene.ID(required=True))
    def resolve_PropertyOwnersBy_id(self, info, **kwargs):
        return models.PropertyOwners.objects.get(**kwargs)
            