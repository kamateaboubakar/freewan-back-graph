from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .qr_codes.types import QrCodesType, QrCodesFilter

class QrCodesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.QrCodes
        fields = {field.name:['exact'] for field in models.QrCodes._meta.fields}
    
        exclude = ['details']
            
class QrCodesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.QrCodes
        filterset_class = QrCodesFilter
        interfaces = (graphene.relay.Node,)
            