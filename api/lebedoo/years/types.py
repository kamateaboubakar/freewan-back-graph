from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .years.types import YearsType, YearsFilter

class YearsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Years
        fields = {field.name:['exact'] for field in models.Years._meta.fields}
    
        
class YearsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Years
        filterset_class = YearsFilter
        interfaces = (graphene.relay.Node,)
            