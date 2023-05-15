from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .users_security_questions.types import UsersSecurityQuestionsType, UsersSecurityQuestionsFilter

class UsersSecurityQuestionsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.UsersSecurityQuestions
        fields = {field.name:['exact'] for field in models.UsersSecurityQuestions._meta.fields}
    
        
class UsersSecurityQuestionsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.UsersSecurityQuestions
        filterset_class = UsersSecurityQuestionsFilter
        interfaces = (graphene.relay.Node,)
            