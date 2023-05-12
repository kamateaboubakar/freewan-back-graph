import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .rental_payments.types import RentalPaymentsType, RentalPaymentsFilter 
# from .rental_payments import queries as rental_payments_queries, mutations as rental_payments_mutations       
#    create_rental_payments = rental_payments_mutations.InsertRentalPayments.Field()
#    update_rental_payments = rental_payments_mutations.UpdateRentalPayments.Field()
#    rental_payments_queries.RentalPaymentsQuery,


# 
# ********************* insertion class *********************
class InsertRentalPayments(graphene.Mutation):
    success = graphene.Boolean()
    rental_payments = graphene.Field(types.RentalPaymentsType)
    errors = graphene.String()

    class Arguments:

        amount = graphene.Float()
                    
        payments_details = graphene.JSONString(required=True)
                    
        month = graphene.ID(required=True)
                    
        year = graphene.ID(required=True)
                    
        property = graphene.ID(required=True)
                    
        property_owner = graphene.ID(required=True)
                    
        property_tenant = graphene.ID(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createRentalPayments(amount:0.3185711111401426, paymentsDetails:""{"key":"value"}"", month:, year:, property:, propertyOwner:, propertyTenant:, addedBy:)
        > {
>                success
>                errors
>                rentalPayments   
        >             { 
>                                id 
>                                amount 
>                                paymentsDetails 
>                            month 
>                                {
>                                    id
>                                } 
>                            year 
>                                {
>                                    id
>                                } 
>                            property 
>                                {
>                                    id
>                                } 
>                            propertyOwner 
>                                {
>                                    id
>                                } 
>                            propertyTenant 
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
        
            kwargs['month'] = models.Months.objects.get(id=kwargs['month'])
                    
            kwargs['year'] = models.Years.objects.get(id=kwargs['year'])
                    
            kwargs['property'] = models.Property.objects.get(id=kwargs['property'])
                    
            kwargs['property_owner'] = models.PropertyOwners.objects.get(id=kwargs['property_owner'])
                    
            kwargs['property_tenant'] = models.PropertyTenants.objects.get(id=kwargs['property_tenant'])
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.RentalPayments.objects.create(**kwargs)
            return InsertRentalPayments(rental_payments=models.RentalPayments.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertRentalPayments(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateRentalPayments(graphene.Mutation):
    success = graphene.Boolean()
    rental_payments = graphene.Field(types.RentalPaymentsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        amount = graphene.Float()
                    
        payments_details = graphene.JSONString()
                    
        month = graphene.ID(required=True)
                    
        year = graphene.ID(required=True)
                    
        property = graphene.ID(required=True)
                    
        property_owner = graphene.ID(required=True)
                    
        property_tenant = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateRentalPayments(id:"", amount:0.5821984632747204, paymentsDetails:{"key":"value"}, month:, year:, property:, propertyOwner:, propertyTenant:, isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                rentalPayments   
        >            { 
                            >    id 
                            >    amount 
                            >    paymentsDetails 
                            month 
                                {
>                                    id
                                } 
                            year 
                                {
>                                    id
                                } 
                            property 
                                {
>                                    id
                                } 
                            propertyOwner 
                                {
>                                    id
                                } 
                            propertyTenant 
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
        
            kwargs['id'] = models.RentalPayments.objects.get(id=kwargs['id']).id
                    
            kwargs['month'] = models.Months.objects.get(id=kwargs['month']).id
                    
            kwargs['year'] = models.Years.objects.get(id=kwargs['year']).id
                    
            kwargs['property'] = models.Property.objects.get(id=kwargs['property']).id
                    
            kwargs['property_owner'] = models.PropertyOwners.objects.get(id=kwargs['property_owner']).id
                    
            kwargs['property_tenant'] = models.PropertyTenants.objects.get(id=kwargs['property_tenant']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.RentalPayments.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateRentalPayments(rental_payments=models.RentalPayments.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateRentalPayments(errors=error, success=False)
        