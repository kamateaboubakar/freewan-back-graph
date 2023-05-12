import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .roles_privileges.types import RolesPrivilegesType, RolesPrivilegesFilter 
# from .roles_privileges import queries as roles_privileges_queries, mutations as roles_privileges_mutations       
#    create_roles_privileges = roles_privileges_mutations.InsertRolesPrivileges.Field()
#    update_roles_privileges = roles_privileges_mutations.UpdateRolesPrivileges.Field()
#    roles_privileges_queries.RolesPrivilegesQuery,


# 
# ********************* insertion class *********************
class InsertRolesPrivileges(graphene.Mutation):
    success = graphene.Boolean()
    roles_privileges = graphene.Field(types.RolesPrivilegesType)
    errors = graphene.String()

    class Arguments:

        privilege = graphene.ID(required=True)
                    
        role = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createRolesPrivileges(privilege:, role:)
        > {
>                success
>                errors
>                rolesPrivileges   
        >             { 
>                                id 
>                            privilege 
>                                {
>                                    id
>                                } 
>                            role 
>                                {
>                                    id
>                                }
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['privilege'] = models.UserPrivileges.objects.get(id=kwargs['privilege'])
                    
            kwargs['role'] = models.UserRoles.objects.get(id=kwargs['role'])
                    
            models.RolesPrivileges.objects.create(**kwargs)
            return InsertRolesPrivileges(roles_privileges=models.RolesPrivileges.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertRolesPrivileges(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateRolesPrivileges(graphene.Mutation):
    success = graphene.Boolean()
    roles_privileges = graphene.Field(types.RolesPrivilegesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        privilege = graphene.ID(required=True)
                    
        role = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateRolesPrivileges(id:"", privilege:, role:){
>                success
>                errors
>                rolesPrivileges   
        >            { 
                            >    id 
                            privilege 
                                {
>                                    id
                                } 
                            role 
                                {
>                                    id
                                }
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.RolesPrivileges.objects.get(id=kwargs['id']).id
                    
            kwargs['privilege'] = models.UserPrivileges.objects.get(id=kwargs['privilege']).id
                    
            kwargs['role'] = models.UserRoles.objects.get(id=kwargs['role']).id
                    
            models.RolesPrivileges.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateRolesPrivileges(roles_privileges=models.RolesPrivileges.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateRolesPrivileges(errors=error, success=False)
        