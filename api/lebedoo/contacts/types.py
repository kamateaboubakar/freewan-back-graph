from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters


# use it in your type.py file like following :
# from .contacts.types import ContactsType, ContactsFilter

class ContactsFilter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.Contacts
        fields = {field.name:['exact'] for field in models.Contacts._meta.fields}
    
        
class ContactsType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.Contacts
        filterset_class = ContactsFilter
        interfaces = (graphene.relay.Node,)
            