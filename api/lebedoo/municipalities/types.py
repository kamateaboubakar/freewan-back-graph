from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .municipalities.types import MunicipalitiesType, MunicipalitiesFilter

class MunicipalitiesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Municipalities
        fields = {field.name:['exact'] for field in models.Municipalities._meta.fields}
    
        
class MunicipalitiesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Municipalities
        filterset_class = MunicipalitiesFilter
        interfaces = (graphene.relay.Node,)
            