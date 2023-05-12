import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .contacts.types import ContactsType, ContactsFilter 
# from .contacts import queries as contacts_queries, mutations as contacts_mutations       
#    create_contacts = contacts_mutations.InsertContacts.Field()
#    update_contacts = contacts_mutations.UpdateContacts.Field()
#    contacts_queries.ContactsQuery,


# 
# ********************* insertion class *********************
class InsertContacts(graphene.Mutation):
    success = graphene.Boolean()
    contacts = graphene.Field(types.ContactsType)
    errors = graphene.String()

    class Arguments:

        users = graphene.ID(required=True)
                    
        country = graphene.ID(required=True)
                    
        phone_number = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createContacts(users:, country:, phoneNumber:"fiqwkmjqfs")
        > {
>                success
>                errors
>                contacts   
        >             { 
>                                id 
>                            users 
>                                {
>                                    id
>                                } 
>                            country 
>                                {
>                                    id
>                                } 
>                                phoneNumber 
>                                isActive 
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
        
            kwargs['users'] = models.Users.objects.get(id=kwargs['users'])
                    
            kwargs['country'] = models.Country.objects.get(id=kwargs['country'])
                    
            models.Contacts.objects.create(**kwargs)
            return InsertContacts(contacts=models.Contacts.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertContacts(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateContacts(graphene.Mutation):
    success = graphene.Boolean()
    contacts = graphene.Field(types.ContactsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        users = graphene.ID(required=True)
                    
        country = graphene.ID(required=True)
                    
        phone_number = graphene.String()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateContacts(id:"", users:, country:, phoneNumber:"zstilkrgwu", isActive:false, isDeleted:false){
>                success
>                errors
>                contacts   
        >            { 
                            >    id 
                            users 
                                {
>                                    id
                                } 
                            country 
                                {
>                                    id
                                } 
                            >    phoneNumber 
                            >    isActive 
                            >    isDeleted 
                            >    createdDate 
                            >    updatedDate
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.Contacts.objects.get(id=kwargs['id']).id
                    
            kwargs['users'] = models.Users.objects.get(id=kwargs['users']).id
                    
            kwargs['country'] = models.Country.objects.get(id=kwargs['country']).id
                    
            models.Contacts.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateContacts(contacts=models.Contacts.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateContacts(errors=error, success=False)
        