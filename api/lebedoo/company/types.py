from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .company.types import CompanyType, CompanyFilter

class CompanyFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Company
        fields = {field.name:['exact'] for field in models.Company._meta.fields}
    
        exclude = ['address', 'contact', 'area']
            
class CompanyType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Company
        filterset_class = CompanyFilter
        interfaces = (graphene.relay.Node,)
            