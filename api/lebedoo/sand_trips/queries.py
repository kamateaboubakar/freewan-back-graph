import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .sand_trips import queries as sand_trips_queries
# sand_trips_queries.SandTripsQuery,

class SandTripsQuery(graphene.ObjectType):
        
    SandTripsNode = DjangoFilterConnectionField(types.SandTripsType, filterset_class=types.SandTripsFilter)
    def resolve_SandTripsNode(self, info, **kwargs):
        pass
            
    SandTripsBy_id = graphene.Field(types.SandTripsType, id=graphene.ID(required=True))
    def resolve_SandTripsBy_id(self, info, **kwargs):
        return models.SandTrips.objects.get(**kwargs)
            