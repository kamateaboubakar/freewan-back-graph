from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .roles_privileges.types import RolesPrivilegesType, RolesPrivilegesFilter

class RolesPrivilegesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.RolesPrivileges
        fields = {field.name:['exact'] for field in models.RolesPrivileges._meta.fields}
    
        
class RolesPrivilegesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.RolesPrivileges
        filterset_class = RolesPrivilegesFilter
        interfaces = (graphene.relay.Node,)
            