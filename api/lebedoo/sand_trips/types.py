from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .sand_trips.types import SandTripsType, SandTripsFilter

class SandTripsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.SandTrips
        fields = {field.name:['exact'] for field in models.SandTrips._meta.fields}
    
        exclude = ['trip_details']
            
class SandTripsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.SandTrips
        filterset_class = SandTripsFilter
        interfaces = (graphene.relay.Node,)
            