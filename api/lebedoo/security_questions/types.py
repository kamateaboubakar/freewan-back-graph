from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .security_questions.types import SecurityQuestionsType, SecurityQuestionsFilter

class SecurityQuestionsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.SecurityQuestions
        fields = {field.name:['exact'] for field in models.SecurityQuestions._meta.fields}
    
        
class SecurityQuestionsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.SecurityQuestions
        filterset_class = SecurityQuestionsFilter
        interfaces = (graphene.relay.Node,)
            