from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .otp_codes.types import OtpCodesType, OtpCodesFilter

class OtpCodesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.OtpCodes
        fields = {field.name:['exact'] for field in models.OtpCodes._meta.fields}
    
        
class OtpCodesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.OtpCodes
        filterset_class = OtpCodesFilter
        interfaces = (graphene.relay.Node,)
            