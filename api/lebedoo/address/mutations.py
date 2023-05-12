import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .address.types import AddressType, AddressFilter 
# from .address import queries as address_queries, mutations as address_mutations       
#    create_address = address_mutations.InsertAddress.Field()
#    update_address = address_mutations.UpdateAddress.Field()
#    address_queries.AddressQuery,


# 
# ********************* insertion class *********************
class InsertAddress(graphene.Mutation):
    success = graphene.Boolean()
    address = graphene.Field(types.AddressType)
    errors = graphene.String()

    class Arguments:

        users = graphene.ID(required=True)
                    
        details = graphene.String()
                    
        municipality = graphene.ID(required=True)
                    
        department = graphene.ID(required=True)
                    
        region = graphene.ID(required=True)
                    
        city = graphene.ID(required=True)
                    
        country = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createAddress(users:, details:"xqwhhwlpqj", municipality:, department:, region:, city:, country:)
        > {
>                success
>                errors
>                address   
        >             { 
>                                id 
>                            users 
>                                {
>                                    id
>                                } 
>                                details 
>                            municipality 
>                                {
>                                    id
>                                } 
>                            department 
>                                {
>                                    id
>                                } 
>                            region 
>                                {
>                                    id
>                                } 
>                            city 
>                                {
>                                    id
>                                } 
>                            country 
>                                {
>                                    id
>                                } 
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
                    
            kwargs['municipality'] = models.Municipalities.objects.get(id=kwargs['municipality'])
                    
            kwargs['department'] = models.Department.objects.get(id=kwargs['department'])
                    
            kwargs['region'] = models.Region.objects.get(id=kwargs['region'])
                    
            kwargs['city'] = models.Cities.objects.get(id=kwargs['city'])
                    
            kwargs['country'] = models.Country.objects.get(id=kwargs['country'])
                    
            models.Address.objects.create(**kwargs)
            return InsertAddress(address=models.Address.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertAddress(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateAddress(graphene.Mutation):
    success = graphene.Boolean()
    address = graphene.Field(types.AddressType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        users = graphene.ID(required=True)
                    
        details = graphene.String()
                    
        municipality = graphene.ID(required=True)
                    
        department = graphene.ID(required=True)
                    
        region = graphene.ID(required=True)
                    
        city = graphene.ID(required=True)
                    
        country = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateAddress(id:"", users:, details:"maxwwtpowj", municipality:, department:, region:, city:, country:, isActive:false, isDeleted:true){
>                success
>                errors
>                address   
        >            { 
                            >    id 
                            users 
                                {
>                                    id
                                } 
                            >    details 
                            municipality 
                                {
>                                    id
                                } 
                            department 
                                {
>                                    id
                                } 
                            region 
                                {
>                                    id
                                } 
                            city 
                                {
>                                    id
                                } 
                            country 
                                {
>                                    id
                                } 
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
        
            kwargs['id'] = models.Address.objects.get(id=kwargs['id']).id
                    
            kwargs['users'] = models.Users.objects.get(id=kwargs['users']).id
                    
            kwargs['municipality'] = models.Municipalities.objects.get(id=kwargs['municipality']).id
                    
            kwargs['department'] = models.Department.objects.get(id=kwargs['department']).id
                    
            kwargs['region'] = models.Region.objects.get(id=kwargs['region']).id
                    
            kwargs['city'] = models.Cities.objects.get(id=kwargs['city']).id
                    
            kwargs['country'] = models.Country.objects.get(id=kwargs['country']).id
                    
            models.Address.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateAddress(address=models.Address.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateAddress(errors=error, success=False)
        