import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .company import queries as company_queries
# company_queries.CompanyQuery,

class CompanyQuery(graphene.ObjectType):
        
    CompanyNode = DjangoFilterConnectionField(types.CompanyType, filterset_class=types.CompanyFilter)
    def resolve_CompanyNode(self, info, **kwargs):
        pass
            
    CompanyBy_id = graphene.Field(types.CompanyType, id=graphene.ID(required=True))
    def resolve_CompanyBy_id(self, info, **kwargs):
        return models.Company.objects.get(**kwargs)
            