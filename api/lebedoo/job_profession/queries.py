import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .job_profession import queries as job_profession_queries
# job_profession_queries.JobProfessionQuery,

class JobProfessionQuery(graphene.ObjectType):
        
    JobProfessionNode = DjangoFilterConnectionField(types.JobProfessionType, filterset_class=types.JobProfessionFilter)
    def resolve_JobProfessionNode(self, info, **kwargs):
        pass
            
    JobProfessionBy_id = graphene.Field(types.JobProfessionType, id=graphene.ID(required=True))
    def resolve_JobProfessionBy_id(self, info, **kwargs):
        return models.JobProfession.objects.get(**kwargs)
            