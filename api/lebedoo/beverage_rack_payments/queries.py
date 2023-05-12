import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .beverage_rack_payments import queries as beverage_rack_payments_queries
# beverage_rack_payments_queries.BeverageRackPaymentsQuery,

class BeverageRackPaymentsQuery(graphene.ObjectType):
        
    BeverageRackPaymentsNode = DjangoFilterConnectionField(types.BeverageRackPaymentsType, filterset_class=types.BeverageRackPaymentsFilter)
    def resolve_BeverageRackPaymentsNode(self, info, **kwargs):
        pass
            
    BeverageRackPaymentsBy_id = graphene.Field(types.BeverageRackPaymentsType, id=graphene.ID(required=True))
    def resolve_BeverageRackPaymentsBy_id(self, info, **kwargs):
        return models.BeverageRackPayments.objects.get(**kwargs)
            