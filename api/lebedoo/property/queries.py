import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .property import queries as property_queries
# property_queries.PropertyQuery,

class PropertyQuery(graphene.ObjectType):
        
    PropertyNode = DjangoFilterConnectionField(types.PropertyType, filterset_class=types.PropertyFilter)
    def resolve_PropertyNode(self, info, **kwargs):
        pass
            
    PropertyBy_id = graphene.Field(types.PropertyType, id=graphene.ID(required=True))
    def resolve_PropertyBy_id(self, info, **kwargs):
        return models.Property.objects.get(**kwargs)
            