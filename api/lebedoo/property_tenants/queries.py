import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .property_tenants import queries as property_tenants_queries
# property_tenants_queries.PropertyTenantsQuery,

class PropertyTenantsQuery(graphene.ObjectType):
        
    PropertyTenantsNode = DjangoFilterConnectionField(types.PropertyTenantsType, filterset_class=types.PropertyTenantsFilter)
    def resolve_PropertyTenantsNode(self, info, **kwargs):
        pass
            
    PropertyTenantsBy_id = graphene.Field(types.PropertyTenantsType, id=graphene.ID(required=True))
    def resolve_PropertyTenantsBy_id(self, info, **kwargs):
        return models.PropertyTenants.objects.get(**kwargs)
            