import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models


# use it in your schema like following:
# from .transactions import queries as transactions_queries
# transactions_queries.TransactionsQuery,

class TransactionsQuery(graphene.ObjectType):
        
    TransactionsNode = DjangoFilterConnectionField(types.TransactionsType, filterset_class=types.TransactionsFilter)
    def resolve_TransactionsNode(self, info, **kwargs):
        pass
            
    TransactionsBy_id = graphene.Field(types.TransactionsType, id=graphene.ID(required=True))
    def resolve_TransactionsBy_id(self, info, **kwargs):
        return models.Transactions.objects.get(**kwargs)
            