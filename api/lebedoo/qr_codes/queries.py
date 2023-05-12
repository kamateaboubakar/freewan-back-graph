import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .qr_codes import queries as qr_codes_queries
# qr_codes_queries.QrCodesQuery,

class QrCodesQuery(graphene.ObjectType):
        
    QrCodesNode = DjangoFilterConnectionField(types.QrCodesType, filterset_class=types.QrCodesFilter)
    def resolve_QrCodesNode(self, info, **kwargs):
        pass
            
    QrCodesBy_id = graphene.Field(types.QrCodesType, id=graphene.ID(required=True))
    def resolve_QrCodesBy_id(self, info, **kwargs):
        return models.QrCodes.objects.get(**kwargs)
            