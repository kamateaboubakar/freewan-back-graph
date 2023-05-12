from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .job_function.types import JobFunctionType, JobFunctionFilter

class JobFunctionFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.JobFunction
        fields = {field.name:['exact'] for field in models.JobFunction._meta.fields}
    
        
class JobFunctionType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.JobFunction
        filterset_class = JobFunctionFilter
        interfaces = (graphene.relay.Node,)
            