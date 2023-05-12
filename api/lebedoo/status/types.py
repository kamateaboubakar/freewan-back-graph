from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .status.types import StatusType, StatusFilter

class StatusFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Status
        fields = {field.name:['exact'] for field in models.Status._meta.fields}
    
        
class StatusType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Status
        filterset_class = StatusFilter
        interfaces = (graphene.relay.Node,)
            