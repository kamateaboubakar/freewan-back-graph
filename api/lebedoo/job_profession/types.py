from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .job_profession.types import JobProfessionType, JobProfessionFilter

class JobProfessionFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.JobProfession
        fields = {field.name:['exact'] for field in models.JobProfession._meta.fields}
    
        
class JobProfessionType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.JobProfession
        filterset_class = JobProfessionFilter
        interfaces = (graphene.relay.Node,)
            