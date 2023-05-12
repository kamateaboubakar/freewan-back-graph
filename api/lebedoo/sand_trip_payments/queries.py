import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .sand_trip_payments import queries as sand_trip_payments_queries
# sand_trip_payments_queries.SandTripPaymentsQuery,

class SandTripPaymentsQuery(graphene.ObjectType):
        
    SandTripPaymentsNode = DjangoFilterConnectionField(types.SandTripPaymentsType, filterset_class=types.SandTripPaymentsFilter)
    def resolve_SandTripPaymentsNode(self, info, **kwargs):
        pass
            
    SandTripPaymentsBy_id = graphene.Field(types.SandTripPaymentsType, id=graphene.ID(required=True))
    def resolve_SandTripPaymentsBy_id(self, info, **kwargs):
        return models.SandTripPayments.objects.get(**kwargs)
            