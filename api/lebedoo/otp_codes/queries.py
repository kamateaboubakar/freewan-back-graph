import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .otp_codes import queries as otp_codes_queries
# otp_codes_queries.OtpCodesQuery,

class OtpCodesQuery(graphene.ObjectType):
        
    OtpCodesNode = DjangoFilterConnectionField(types.OtpCodesType, filterset_class=types.OtpCodesFilter)
    def resolve_OtpCodesNode(self, info, **kwargs):
        pass
            
    OtpCodesBy_id = graphene.Field(types.OtpCodesType, id=graphene.ID(required=True))
    def resolve_OtpCodesBy_id(self, info, **kwargs):
        return models.OtpCodes.objects.get(**kwargs)
            