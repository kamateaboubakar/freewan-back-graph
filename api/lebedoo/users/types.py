from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .users.types import UsersType, UsersFilter

class UsersFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Users
        fields = {field.name:['exact'] for field in models.Users._meta.fields}
    
        exclude = ['privileges']
            
class UsersType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Users
        filterset_class = UsersFilter
        interfaces = (graphene.relay.Node,)
            