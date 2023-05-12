import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .property_owners.types import PropertyOwnersType, PropertyOwnersFilter 
# from .property_owners import queries as property_owners_queries, mutations as property_owners_mutations       
#    create_property_owners = property_owners_mutations.InsertPropertyOwners.Field()
#    update_property_owners = property_owners_mutations.UpdatePropertyOwners.Field()
#    property_owners_queries.PropertyOwnersQuery,


# 
# ********************* insertion class *********************
class InsertPropertyOwners(graphene.Mutation):
    success = graphene.Boolean()
    property_owners = graphene.Field(types.PropertyOwnersType)
    errors = graphene.String()

    class Arguments:

        property = graphene.ID(required=True)
                    
        property_owner = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createPropertyOwners(property:, propertyOwner:)
        > {
>                success
>                errors
>                propertyOwners   
        >             { 
>                                id 
>                            property 
>                                {
>                                    id
>                                } 
>                            propertyOwner 
>                                {
>                                    id
>                                } 
>                                isActive 
>                                isDeleted
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['property'] = models.Property.objects.get(id=kwargs['property'])
                    
            kwargs['property_owner'] = models.Users.objects.get(id=kwargs['property_owner'])
                    
            models.PropertyOwners.objects.create(**kwargs)
            return InsertPropertyOwners(property_owners=models.PropertyOwners.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertPropertyOwners(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdatePropertyOwners(graphene.Mutation):
    success = graphene.Boolean()
    property_owners = graphene.Field(types.PropertyOwnersType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        property = graphene.ID(required=True)
                    
        property_owner = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updatePropertyOwners(id:"", property:, propertyOwner:, isActive:false, isDeleted:true){
>                success
>                errors
>                propertyOwners   
        >            { 
                            >    id 
                            property 
                                {
>                                    id
                                } 
                            propertyOwner 
                                {
>                                    id
                                } 
                            >    isActive 
                            >    isDeleted
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.PropertyOwners.objects.get(id=kwargs['id']).id
                    
            kwargs['property'] = models.Property.objects.get(id=kwargs['property']).id
                    
            kwargs['property_owner'] = models.Users.objects.get(id=kwargs['property_owner']).id
                    
            models.PropertyOwners.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdatePropertyOwners(property_owners=models.PropertyOwners.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdatePropertyOwners(errors=error, success=False)
        