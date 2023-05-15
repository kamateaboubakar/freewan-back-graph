import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .users.types import UsersType, UsersFilter 
# from .users import queries as users_queries, mutations as users_mutations       
#    create_users = users_mutations.InsertUsers.Field()
#    update_users = users_mutations.UpdateUsers.Field()
#    users_queries.UsersQuery,


# 
# ********************* insertion class *********************
class InsertUsers(graphene.Mutation):
    success = graphene.Boolean()
    users = graphene.Field(types.UsersType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        username = graphene.String()
                    
        email = graphene.String()
                    
        phone_number = graphene.String()
                    
        country_code = graphene.ID(required=True)
                    
        first_name = graphene.String()
                    
        last_name = graphene.String()
                    
        # privileges = graphene.JSONString(required=True)
                    
        is_admin = graphene.Boolean()
                    
        is_freelancer = graphene.Boolean()
                    
        is_client = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        > createUsers(id:"", username:"fdthwbkxsh", email:"szcqvowsso", phoneNumber:"qphcdazklr", countryCode:, firstName:"jcdkjylhvn", lastName:"eadkyxuvor", privileges:"""{"role":"state"}""", isAdmin:true, isFreelancer:true, isClient:false)
        > {
>                success
>                errors
>                users   
        >             { 
>                                id 
>                                username 
>                                email 
>                                phoneNumber 
>                            countryCode 
>                                {
>                                    id
>                                } 
>                                firstName 
>                                lastName 
>                                privileges 
>                                isAdmin 
>                                isFreelancer 
>                                isClient 
>                                isDeleted 
>                                createdDate 
>                                updatedDate
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['country_code'] = models.Country.objects.get(id=kwargs['country_code'])
                    
            models.Users.objects.create(**kwargs)
            return InsertUsers(users=models.Users.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertUsers(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateUsers(graphene.Mutation):
    success = graphene.Boolean()
    users = graphene.Field(types.UsersType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        username = graphene.String()
                    
        email = graphene.String()
                    
        phone_number = graphene.String()
                    
        country_code = graphene.ID(required=True)
                    
        first_name = graphene.String()
                    
        last_name = graphene.String()
                    
        privileges = graphene.JSONString(required=True)
                    
        is_admin = graphene.Boolean()
                    
        is_freelancer = graphene.Boolean()
                    
        is_client = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateUsers(id:"", username:"bqrrdpxluw", email:"uoivvlwoym", phoneNumber:"jatszejjic", countryCode:, firstName:"vflxdsrvmo", lastName:"gystiasblv", privileges:{"role":"state"}, isAdmin:true, isFreelancer:true, isClient:true, isDeleted:false){
>                success
>                errors
>                users   
        >            { 
                            >    id 
                            >    username 
                            >    email 
                            >    phoneNumber 
                            countryCode 
                                {
>                                    id
                                } 
                            >    firstName 
                            >    lastName 
                            >    privileges 
                            >    isAdmin 
                            >    isFreelancer 
                            >    isClient 
                            >    isDeleted 
                            >    createdDate 
                            >    updatedDate
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.Users.objects.get(id=kwargs['id']).id
                    
            kwargs['country_code'] = models.Country.objects.get(id=kwargs['country_code']).id
                    
            models.Users.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateUsers(users=models.Users.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateUsers(errors=error, success=False)
        