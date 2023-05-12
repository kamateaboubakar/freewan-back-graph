from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .transactions.types import TransactionsType, TransactionsFilter

class TransactionsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Transactions
        fields = {field.name:['exact'] for field in models.Transactions._meta.fields}
    
        exclude = ['metadata']
            
class TransactionsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Transactions
        filterset_class = TransactionsFilter
        interfaces = (graphene.relay.Node,)
            