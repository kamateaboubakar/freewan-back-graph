from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .continent.types import ContinentType, ContinentFilter

class ContinentFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Continent
        fields = {field.name:['exact'] for field in models.Continent._meta.fields}
    
        
class ContinentType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Continent
        filterset_class = ContinentFilter
        interfaces = (graphene.relay.Node,)
            