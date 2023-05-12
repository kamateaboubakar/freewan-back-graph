import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .user_roles.types import UserRolesType, UserRolesFilter 
# from .user_roles import queries as user_roles_queries, mutations as user_roles_mutations       
#    create_user_roles = user_roles_mutations.InsertUserRoles.Field()
#    update_user_roles = user_roles_mutations.UpdateUserRoles.Field()
#    user_roles_queries.UserRolesQuery,


# 
# ********************* insertion class *********************
class InsertUserRoles(graphene.Mutation):
    success = graphene.Boolean()
    user_roles = graphene.Field(types.UserRolesType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createUserRoles(name:"zebaulkpyb",)
        > {
>                success
>                errors
>                userRoles   
        >             { 
>                                id 
>                                name 
>                                isDeleted
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            models.UserRoles.objects.create(**kwargs)
            return InsertUserRoles(user_roles=models.UserRoles.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertUserRoles(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateUserRoles(graphene.Mutation):
    success = graphene.Boolean()
    user_roles = graphene.Field(types.UserRolesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateUserRoles(id:"", name:"kndvkgwvsx", isDeleted:false){
>                success
>                errors
>                userRoles   
        >            { 
                            >    id 
                            >    name 
                            >    isDeleted
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.UserRoles.objects.get(id=kwargs['id']).id
                    
            models.UserRoles.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateUserRoles(user_roles=models.UserRoles.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateUserRoles(errors=error, success=False)
        