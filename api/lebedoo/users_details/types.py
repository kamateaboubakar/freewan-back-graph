from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .users_details.types import UsersDetailsType, UsersDetailsFilter

class UsersDetailsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.UsersDetails
        fields = {field.name:['exact'] for field in models.UsersDetails._meta.fields}
    
        exclude = ['address', 'contacts', 'languages', 'skills', 'experiences', 'links', 'degrees']
            
class UsersDetailsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.UsersDetails
        filterset_class = UsersDetailsFilter
        interfaces = (graphene.relay.Node,)
            