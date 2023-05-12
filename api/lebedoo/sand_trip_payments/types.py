from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .sand_trip_payments.types import SandTripPaymentsType, SandTripPaymentsFilter

class SandTripPaymentsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.SandTripPayments
        fields = {field.name:['exact'] for field in models.SandTripPayments._meta.fields}
    
        exclude = ['payments_infos']
            
class SandTripPaymentsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.SandTripPayments
        filterset_class = SandTripPaymentsFilter
        interfaces = (graphene.relay.Node,)
            