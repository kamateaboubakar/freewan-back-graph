import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .payment_methods import queries as payment_methods_queries
# payment_methods_queries.PaymentMethodsQuery,

class PaymentMethodsQuery(graphene.ObjectType):
        
    PaymentMethodsNode = DjangoFilterConnectionField(types.PaymentMethodsType, filterset_class=types.PaymentMethodsFilter)
    def resolve_PaymentMethodsNode(self, info, **kwargs):
        pass
            
    PaymentMethodsBy_id = graphene.Field(types.PaymentMethodsType, id=graphene.ID(required=True))
    def resolve_PaymentMethodsBy_id(self, info, **kwargs):
        return models.PaymentMethods.objects.get(**kwargs)
            