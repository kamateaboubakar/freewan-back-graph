from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .department.types import DepartmentType, DepartmentFilter

class DepartmentFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Department
        fields = {field.name:['exact'] for field in models.Department._meta.fields}
    
        
class DepartmentType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Department
        filterset_class = DepartmentFilter
        interfaces = (graphene.relay.Node,)
            