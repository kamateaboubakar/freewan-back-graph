from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .cities.types import CitiesType, CitiesFilter

class CitiesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Cities
        fields = {field.name:['exact'] for field in models.Cities._meta.fields}
    
        
class CitiesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Cities
        filterset_class = CitiesFilter
        interfaces = (graphene.relay.Node,)
            