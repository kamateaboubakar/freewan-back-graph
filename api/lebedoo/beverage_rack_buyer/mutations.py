import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .beverage_rack_buyer.types import BeverageRackBuyerType, BeverageRackBuyerFilter 
# from .beverage_rack_buyer import queries as beverage_rack_buyer_queries, mutations as beverage_rack_buyer_mutations       
#    create_beverage_rack_buyer = beverage_rack_buyer_mutations.InsertBeverageRackBuyer.Field()
#    update_beverage_rack_buyer = beverage_rack_buyer_mutations.UpdateBeverageRackBuyer.Field()
#    beverage_rack_buyer_queries.BeverageRackBuyerQuery,


# 
# ********************* insertion class *********************
class InsertBeverageRackBuyer(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack_buyer = graphene.Field(types.BeverageRackBuyerType)
    errors = graphene.String()

    class Arguments:

        rack = graphene.ID(required=True)
                    
        rack_buyer = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createBeverageRackBuyer(rack:, rackBuyer:)
        > {
>                success
>                errors
>                beverageRackBuyer   
        >             { 
>                                id 
>                            rack 
>                                {
>                                    id
>                                } 
>                            rackBuyer 
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
                    
            kwargs['rack_buyer'] = models.Users.objects.get(id=kwargs['rack_buyer'])
                    
            models.BeverageRackBuyer.objects.create(**kwargs)
            return InsertBeverageRackBuyer(beverage_rack_buyer=models.BeverageRackBuyer.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertBeverageRackBuyer(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateBeverageRackBuyer(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack_buyer = graphene.Field(types.BeverageRackBuyerType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        rack = graphene.ID(required=True)
                    
        rack_buyer = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateBeverageRackBuyer(id:"", rack:, rackBuyer:, isActive:false, isDeleted:false){
>                success
>                errors
>                beverageRackBuyer   
        >            { 
                            >    id 
                            rack 
                                {
>                                    id
                                } 
                            rackBuyer 
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
        
            kwargs['id'] = models.BeverageRackBuyer.objects.get(id=kwargs['id']).id
                    
            kwargs['rack'] = models.BeverageRack.objects.get(id=kwargs['rack']).id
                    
            kwargs['rack_buyer'] = models.Users.objects.get(id=kwargs['rack_buyer']).id
                    
            models.BeverageRackBuyer.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateBeverageRackBuyer(beverage_rack_buyer=models.BeverageRackBuyer.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateBeverageRackBuyer(errors=error, success=False)
        