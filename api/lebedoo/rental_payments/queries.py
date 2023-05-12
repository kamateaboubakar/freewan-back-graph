import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .rental_payments import queries as rental_payments_queries
# rental_payments_queries.RentalPaymentsQuery,

class RentalPaymentsQuery(graphene.ObjectType):
        
    RentalPaymentsNode = DjangoFilterConnectionField(types.RentalPaymentsType, filterset_class=types.RentalPaymentsFilter)
    def resolve_RentalPaymentsNode(self, info, **kwargs):
        pass
            
    RentalPaymentsBy_id = graphene.Field(types.RentalPaymentsType, id=graphene.ID(required=True))
    def resolve_RentalPaymentsBy_id(self, info, **kwargs):
        return models.RentalPayments.objects.get(**kwargs)
            