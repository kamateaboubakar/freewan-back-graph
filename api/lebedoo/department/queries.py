import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .department import queries as department_queries
# department_queries.DepartmentQuery,

class DepartmentQuery(graphene.ObjectType):
        
    DepartmentNode = DjangoFilterConnectionField(types.DepartmentType, filterset_class=types.DepartmentFilter)
    def resolve_DepartmentNode(self, info, **kwargs):
        pass
            
    DepartmentBy_id = graphene.Field(types.DepartmentType, id=graphene.ID(required=True))
    def resolve_DepartmentBy_id(self, info, **kwargs):
        return models.Department.objects.get(**kwargs)
            