import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .beverage_rack_owner.types import BeverageRackOwnerType, BeverageRackOwnerFilter 
# from .beverage_rack_owner import queries as beverage_rack_owner_queries, mutations as beverage_rack_owner_mutations       
#    create_beverage_rack_owner = beverage_rack_owner_mutations.InsertBeverageRackOwner.Field()
#    update_beverage_rack_owner = beverage_rack_owner_mutations.UpdateBeverageRackOwner.Field()
#    beverage_rack_owner_queries.BeverageRackOwnerQuery,


# 
# ********************* insertion class *********************
class InsertBeverageRackOwner(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack_owner = graphene.Field(types.BeverageRackOwnerType)
    errors = graphene.String()

    class Arguments:

        rack = graphene.ID(required=True)
                    
        rack_owner = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createBeverageRackOwner(rack:, rackOwner:)
        > {
>                success
>                errors
>                beverageRackOwner   
        >             { 
>                                id 
>                            rack 
>                                {
>                                    id
>                                } 
>                            rackOwner 
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
        
            kwargs['rack'] = models.BeverageRack.objects.get(id=kwargs['rack'])
                    
            kwargs['rack_owner'] = models.Users.objects.get(id=kwargs['rack_owner'])
                    
            models.BeverageRackOwner.objects.create(**kwargs)
            return InsertBeverageRackOwner(beverage_rack_owner=models.BeverageRackOwner.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertBeverageRackOwner(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateBeverageRackOwner(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack_owner = graphene.Field(types.BeverageRackOwnerType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        rack = graphene.ID(required=True)
                    
        rack_owner = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateBeverageRackOwner(id:"", rack:, rackOwner:, isActive:false, isDeleted:true){
>                success
>                errors
>                beverageRackOwner   
        >            { 
                            >    id 
                            rack 
                                {
>                                    id
                                } 
                            rackOwner 
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
        
            kwargs['id'] = models.BeverageRackOwner.objects.get(id=kwargs['id']).id
                    
            kwargs['rack'] = models.BeverageRack.objects.get(id=kwargs['rack']).id
                    
            kwargs['rack_owner'] = models.Users.objects.get(id=kwargs['rack_owner']).id
                    
            models.BeverageRackOwner.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateBeverageRackOwner(beverage_rack_owner=models.BeverageRackOwner.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateBeverageRackOwner(errors=error, success=False)
        