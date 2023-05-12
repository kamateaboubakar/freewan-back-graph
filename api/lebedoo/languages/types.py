from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .languages.types import LanguagesType, LanguagesFilter

class LanguagesFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Languages
        fields = {field.name:['exact'] for field in models.Languages._meta.fields}
    
        
class LanguagesType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Languages
        filterset_class = LanguagesFilter
        interfaces = (graphene.relay.Node,)
            