from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .beverage_rack_payments.types import BeverageRackPaymentsType, BeverageRackPaymentsFilter

class BeverageRackPaymentsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.BeverageRackPayments
        fields = {field.name:['exact'] for field in models.BeverageRackPayments._meta.fields}
    
        exclude = ['payments_details']
            
class BeverageRackPaymentsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.BeverageRackPayments
        filterset_class = BeverageRackPaymentsFilter
        interfaces = (graphene.relay.Node,)
            