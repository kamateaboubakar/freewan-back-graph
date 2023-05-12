import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .status import queries as status_queries
# status_queries.StatusQuery,

class StatusQuery(graphene.ObjectType):
        
    StatusNode = DjangoFilterConnectionField(types.StatusType, filterset_class=types.StatusFilter)
    def resolve_StatusNode(self, info, **kwargs):
        pass
            
    StatusBy_id = graphene.Field(types.StatusType, id=graphene.ID(required=True))
    def resolve_StatusBy_id(self, info, **kwargs):
        return models.Status.objects.get(**kwargs)
            