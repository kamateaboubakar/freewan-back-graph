import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .beverage_rack_payments.types import BeverageRackPaymentsType, BeverageRackPaymentsFilter 
# from .beverage_rack_payments import queries as beverage_rack_payments_queries, mutations as beverage_rack_payments_mutations       
#    create_beverage_rack_payments = beverage_rack_payments_mutations.InsertBeverageRackPayments.Field()
#    update_beverage_rack_payments = beverage_rack_payments_mutations.UpdateBeverageRackPayments.Field()
#    beverage_rack_payments_queries.BeverageRackPaymentsQuery,


# 
# ********************* insertion class *********************
class InsertBeverageRackPayments(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack_payments = graphene.Field(types.BeverageRackPaymentsType)
    errors = graphene.String()

    class Arguments:

        amount = graphene.Float()
                    
        payments_details = graphene.JSONString(required=True)
                    
        rack = graphene.ID(required=True)
                    
        rack_owner = graphene.ID(required=True)
                    
        rack_buyer = graphene.ID(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createBeverageRackPayments(amount:0.6210780835589742, paymentsDetails:""{"key":"value"}"", rack:, rackOwner:, rackBuyer:, addedBy:)
        > {
>                success
>                errors
>                beverageRackPayments   
        >             { 
>                                id 
>                                amount 
>                                paymentsDetails 
>                            rack 
>                                {
>                                    id
>                                } 
>                            rackOwner 
>                                {
>                                    id
>                                } 
>                            rackBuyer 
>                                {
>                                    id
>                                } 
>                                isActive 
>                                isDeleted 
>                            addedBy 
>                                {
>                                    id
>                                } 
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
                    
            kwargs['rack_owner'] = models.BeverageRackOwner.objects.get(id=kwargs['rack_owner'])
                    
            kwargs['rack_buyer'] = models.BeverageRackBuyer.objects.get(id=kwargs['rack_buyer'])
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.BeverageRackPayments.objects.create(**kwargs)
            return InsertBeverageRackPayments(beverage_rack_payments=models.BeverageRackPayments.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertBeverageRackPayments(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateBeverageRackPayments(graphene.Mutation):
    success = graphene.Boolean()
    beverage_rack_payments = graphene.Field(types.BeverageRackPaymentsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        amount = graphene.Float()
                    
        payments_details = graphene.JSONString()
                    
        rack = graphene.ID(required=True)
                    
        rack_owner = graphene.ID(required=True)
                    
        rack_buyer = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateBeverageRackPayments(id:"", amount:0.9084881233940553, paymentsDetails:{"key":"value"}, rack:, rackOwner:, rackBuyer:, isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                beverageRackPayments   
        >            { 
                            >    id 
                            >    amount 
                            >    paymentsDetails 
                            rack 
                                {
>                                    id
                                } 
                            rackOwner 
                                {
>                                    id
                                } 
                            rackBuyer 
                                {
>                                    id
                                } 
                            >    isActive 
                            >    isDeleted 
                            addedBy 
                                {
>                                    id
                                } 
                            >    createdDate 
                            >    updatedDate
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.BeverageRackPayments.objects.get(id=kwargs['id']).id
                    
            kwargs['rack'] = models.BeverageRack.objects.get(id=kwargs['rack']).id
                    
            kwargs['rack_owner'] = models.BeverageRackOwner.objects.get(id=kwargs['rack_owner']).id
                    
            kwargs['rack_buyer'] = models.BeverageRackBuyer.objects.get(id=kwargs['rack_buyer']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.BeverageRackPayments.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateBeverageRackPayments(beverage_rack_payments=models.BeverageRackPayments.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateBeverageRackPayments(errors=error, success=False)
        