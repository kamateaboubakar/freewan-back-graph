from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .user_roles.types import UserRolesType, UserRolesFilter

class UserRolesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.UserRoles
        fields = {field.name:['exact'] for field in models.UserRoles._meta.fields}
    
        
class UserRolesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.UserRoles
        filterset_class = UserRolesFilter
        interfaces = (graphene.relay.Node,)
            