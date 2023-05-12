from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .region.types import RegionType, RegionFilter

class RegionFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Region
        fields = {field.name:['exact'] for field in models.Region._meta.fields}
    
        
class RegionType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Region
        filterset_class = RegionFilter
        interfaces = (graphene.relay.Node,)
            