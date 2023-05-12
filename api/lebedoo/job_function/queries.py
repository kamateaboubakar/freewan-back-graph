import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .job_function import queries as job_function_queries
# job_function_queries.JobFunctionQuery,

class JobFunctionQuery(graphene.ObjectType):
        
    JobFunctionNode = DjangoFilterConnectionField(types.JobFunctionType, filterset_class=types.JobFunctionFilter)
    def resolve_JobFunctionNode(self, info, **kwargs):
        pass
            
    JobFunctionBy_id = graphene.Field(types.JobFunctionType, id=graphene.ID(required=True))
    def resolve_JobFunctionBy_id(self, info, **kwargs):
        return models.JobFunction.objects.get(**kwargs)
            