import graphene
from .users import queries as users_queries, mutations as users_mutations


class Query(
    users_queries.UsersQuery,

    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_users = users_mutations.InsertUsers.Field()
    update_users = users_mutations.UpdateUsers.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
