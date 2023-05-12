import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .user_privileges.types import UserPrivilegesType, UserPrivilegesFilter 
# from .user_privileges import queries as user_privileges_queries, mutations as user_privileges_mutations       
#    create_user_privileges = user_privileges_mutations.InsertUserPrivileges.Field()
#    update_user_privileges = user_privileges_mutations.UpdateUserPrivileges.Field()
#    user_privileges_queries.UserPrivilegesQuery,


# 
# ********************* insertion class *********************
class InsertUserPrivileges(graphene.Mutation):
    success = graphene.Boolean()
    user_privileges = graphene.Field(types.UserPrivilegesType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createUserPrivileges(name:"jahuslinpv",)
        > {
>                success
>                errors
>                userPrivileges   
        >             { 
>                                id 
>                                name 
>                                isActive 
>                                isDeleted 
>                                createdAt 
>                                updatedAt
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            models.UserPrivileges.objects.create(**kwargs)
            return InsertUserPrivileges(user_privileges=models.UserPrivileges.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertUserPrivileges(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateUserPrivileges(graphene.Mutation):
    success = graphene.Boolean()
    user_privileges = graphene.Field(types.UserPrivilegesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateUserPrivileges(id:"", name:"dnpfnyrsxr", isActive:false, isDeleted:true){
>                success
>                errors
>                userPrivileges   
        >            { 
                            >    id 
                            >    name 
                            >    isActive 
                            >    isDeleted 
                            >    createdAt 
                            >    updatedAt
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.UserPrivileges.objects.get(id=kwargs['id']).id
                    
            models.UserPrivileges.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateUserPrivileges(user_privileges=models.UserPrivileges.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateUserPrivileges(errors=error, success=False)
        