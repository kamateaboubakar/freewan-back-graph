from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .user_privileges.types import UserPrivilegesType, UserPrivilegesFilter

class UserPrivilegesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.UserPrivileges
        fields = {field.name:['exact'] for field in models.UserPrivileges._meta.fields}
    
        
class UserPrivilegesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.UserPrivileges
        filterset_class = UserPrivilegesFilter
        interfaces = (graphene.relay.Node,)
            