from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .sand_infos.types import SandInfosType, SandInfosFilter

class SandInfosFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.SandInfos
        fields = {field.name:['exact'] for field in models.SandInfos._meta.fields}
    
        exclude = ['details']
            
class SandInfosType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.SandInfos
        filterset_class = SandInfosFilter
        interfaces = (graphene.relay.Node,)
            