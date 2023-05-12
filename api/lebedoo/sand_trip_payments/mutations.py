import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .sand_trip_payments.types import SandTripPaymentsType, SandTripPaymentsFilter 
# from .sand_trip_payments import queries as sand_trip_payments_queries, mutations as sand_trip_payments_mutations       
#    create_sand_trip_payments = sand_trip_payments_mutations.InsertSandTripPayments.Field()
#    update_sand_trip_payments = sand_trip_payments_mutations.UpdateSandTripPayments.Field()
#    sand_trip_payments_queries.SandTripPaymentsQuery,


# 
# ********************* insertion class *********************
class InsertSandTripPayments(graphene.Mutation):
    success = graphene.Boolean()
    sand_trip_payments = graphene.Field(types.SandTripPaymentsType)
    errors = graphene.String()

    class Arguments:

        sand_trip = graphene.ID(required=True)
                    
        payments_infos = graphene.JSONString(required=True)
                    
        sand_trip_owners = graphene.ID(required=True)
                    
        sand_trip_buyer = graphene.ID(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createSandTripPayments(sandTrip:, paymentsInfos:""{"key":"value"}"", sandTripOwners:, sandTripBuyer:, addedBy:)
        > {
>                success
>                errors
>                sandTripPayments   
        >             { 
>                                id 
>                            sandTrip 
>                                {
>                                    id
>                                } 
>                                paymentsInfos 
>                            sandTripOwners 
>                                {
>                                    id
>                                } 
>                            sandTripBuyer 
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
        
            kwargs['sand_trip'] = models.SandTrips.objects.get(id=kwargs['sand_trip'])
                    
            kwargs['sand_trip_owners'] = models.SandVendors.objects.get(id=kwargs['sand_trip_owners'])
                    
            kwargs['sand_trip_buyer'] = models.SandBuyer.objects.get(id=kwargs['sand_trip_buyer'])
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.SandTripPayments.objects.create(**kwargs)
            return InsertSandTripPayments(sand_trip_payments=models.SandTripPayments.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertSandTripPayments(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateSandTripPayments(graphene.Mutation):
    success = graphene.Boolean()
    sand_trip_payments = graphene.Field(types.SandTripPaymentsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        sand_trip = graphene.ID(required=True)
                    
        payments_infos = graphene.JSONString()
                    
        sand_trip_owners = graphene.ID(required=True)
                    
        sand_trip_buyer = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateSandTripPayments(id:"", sandTrip:, paymentsInfos:{"key":"value"}, sandTripOwners:, sandTripBuyer:, isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                sandTripPayments   
        >            { 
                            >    id 
                            sandTrip 
                                {
>                                    id
                                } 
                            >    paymentsInfos 
                            sandTripOwners 
                                {
>                                    id
                                } 
                            sandTripBuyer 
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
        
            kwargs['id'] = models.SandTripPayments.objects.get(id=kwargs['id']).id
                    
            kwargs['sand_trip'] = models.SandTrips.objects.get(id=kwargs['sand_trip']).id
                    
            kwargs['sand_trip_owners'] = models.SandVendors.objects.get(id=kwargs['sand_trip_owners']).id
                    
            kwargs['sand_trip_buyer'] = models.SandBuyer.objects.get(id=kwargs['sand_trip_buyer']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.SandTripPayments.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateSandTripPayments(sand_trip_payments=models.SandTripPayments.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateSandTripPayments(errors=error, success=False)
        