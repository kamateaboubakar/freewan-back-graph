from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .payment_methods.types import PaymentMethodsType, PaymentMethodsFilter

class PaymentMethodsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.PaymentMethods
        fields = {field.name:['exact'] for field in models.PaymentMethods._meta.fields}
    
        
class PaymentMethodsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.PaymentMethods
        filterset_class = PaymentMethodsFilter
        interfaces = (graphene.relay.Node,)
            