from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .country.types import CountryType, CountryFilter

class CountryFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Country
        fields = {field.name:['exact'] for field in models.Country._meta.fields}
    
        
class CountryType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Country
        filterset_class = CountryFilter
        interfaces = (graphene.relay.Node,)
            