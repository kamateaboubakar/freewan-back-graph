import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .beverage_rack.types import BeverageRackType, BeverageRackFilter 
# from .beverage_rack import queries as beverage_rack_queries, mutations as beverage_rack_mutations       
#    create_beverage_rack = beverage_rack_mutations.InsertBeverageRack.Field()
#    update_beverage_rack = beverage_rack_mutations.UpdateBeverageRack.Field()
#    beverage_rack_queries.BeverageRackQuery,


# 
# ********************* insertion class *********************
class InsertBeverageRack(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack = graphene.Field(types.BeverageRackType)
    errors = graphene.String()

    class Arguments:

        amount = graphene.Float()
                    
        rack_details = graphene.JSONString(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createBeverageRack(amount:0.9667765521150018, rackDetails:""{"key":"value"}"")
        > {
>                success
>                errors
>                beverageRack   
        >             { 
>                                id 
>                                amount 
>                                rackDetails 
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
        
            models.BeverageRack.objects.create(**kwargs)
            return InsertBeverageRack(beverage_rack=models.BeverageRack.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertBeverageRack(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateBeverageRack(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack = graphene.Field(types.BeverageRackType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        amount = graphene.Float()
                    
        rack_details = graphene.JSONString()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateBeverageRack(id:"", amount:0.8686756283058468, rackDetails:{"key":"value"}, isActive:true, isDeleted:false){
>                success
>                errors
>                beverageRack   
        >            { 
                            >    id 
                            >    amount 
                            >    rackDetails 
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
        
            kwargs['id'] = models.BeverageRack.objects.get(id=kwargs['id']).id
                    
            models.BeverageRack.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateBeverageRack(beverage_rack=models.BeverageRack.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateBeverageRack(errors=error, success=False)
        