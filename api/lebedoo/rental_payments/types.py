from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .rental_payments.types import RentalPaymentsType, RentalPaymentsFilter

class RentalPaymentsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.RentalPayments
        fields = {field.name:['exact'] for field in models.RentalPayments._meta.fields}
    
        exclude = ['payments_details']
            
class RentalPaymentsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.RentalPayments
        filterset_class = RentalPaymentsFilter
        interfaces = (graphene.relay.Node,)
            