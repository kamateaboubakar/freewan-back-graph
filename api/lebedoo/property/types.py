from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .property.types import PropertyType, PropertyFilter

class PropertyFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Property
        fields = {field.name:['exact'] for field in models.Property._meta.fields}
    
        
class PropertyType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Property
        filterset_class = PropertyFilter
        interfaces = (graphene.relay.Node,)
            