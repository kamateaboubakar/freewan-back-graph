import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .property_tenants.types import PropertyTenantsType, PropertyTenantsFilter 
# from .property_tenants import queries as property_tenants_queries, mutations as property_tenants_mutations       
#    create_property_tenants = property_tenants_mutations.InsertPropertyTenants.Field()
#    update_property_tenants = property_tenants_mutations.UpdatePropertyTenants.Field()
#    property_tenants_queries.PropertyTenantsQuery,


# 
# ********************* insertion class *********************
class InsertPropertyTenants(graphene.Mutation):
    success = graphene.Boolean()
    property_tenants = graphene.Field(types.PropertyTenantsType)
    errors = graphene.String()

    class Arguments:

        property = graphene.ID(required=True)
                    
        property_tenant = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createPropertyTenants(property:, propertyTenant:)
        > {
>                success
>                errors
>                propertyTenants   
        >             { 
>                                id 
>                            property 
>                                {
>                                    id
>                                } 
>                            propertyTenant 
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
                    
            kwargs['property_tenant'] = models.Users.objects.get(id=kwargs['property_tenant'])
                    
            models.PropertyTenants.objects.create(**kwargs)
            return InsertPropertyTenants(property_tenants=models.PropertyTenants.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertPropertyTenants(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdatePropertyTenants(graphene.Mutation):
    success = graphene.Boolean()
    property_tenants = graphene.Field(types.PropertyTenantsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        property = graphene.ID(required=True)
                    
        property_tenant = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updatePropertyTenants(id:"", property:, propertyTenant:, isActive:true, isDeleted:false){
>                success
>                errors
>                propertyTenants   
        >            { 
                            >    id 
                            property 
                                {
>                                    id
                                } 
                            propertyTenant 
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
        
            kwargs['id'] = models.PropertyTenants.objects.get(id=kwargs['id']).id
                    
            kwargs['property'] = models.Property.objects.get(id=kwargs['property']).id
                    
            kwargs['property_tenant'] = models.Users.objects.get(id=kwargs['property_tenant']).id
                    
            models.PropertyTenants.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdatePropertyTenants(property_tenants=models.PropertyTenants.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdatePropertyTenants(errors=error, success=False)
        