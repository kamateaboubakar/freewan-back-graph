import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .contacts import queries as contacts_queries
# contacts_queries.ContactsQuery,

class ContactsQuery(graphene.ObjectType):
        
    ContactsNode = DjangoFilterConnectionField(types.ContactsType, filterset_class=types.ContactsFilter)
    def resolve_ContactsNode(self, info, **kwargs):
        pass
            
    ContactsBy_id = graphene.Field(types.ContactsType, id=graphene.ID(required=True))
    def resolve_ContactsBy_id(self, info, **kwargs):
        return models.Contacts.objects.get(**kwargs)
            