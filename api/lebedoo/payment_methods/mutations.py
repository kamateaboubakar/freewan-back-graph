import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .payment_methods.types import PaymentMethodsType, PaymentMethodsFilter 
# from .payment_methods import queries as payment_methods_queries, mutations as payment_methods_mutations       
#    create_payment_methods = payment_methods_mutations.InsertPaymentMethods.Field()
#    update_payment_methods = payment_methods_mutations.UpdatePaymentMethods.Field()
#    payment_methods_queries.PaymentMethodsQuery,


# 
# ********************* insertion class *********************
class InsertPaymentMethods(graphene.Mutation):
    success = graphene.Boolean()
    payment_methods = graphene.Field(types.PaymentMethodsType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createPaymentMethods(name:"gclojtwxgm", abbreviated:"ozgjyauqra", addedBy:)
        > {
>                success
>                errors
>                paymentMethods   
        >             { 
>                                id 
>                                name 
>                                abbreviated 
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
        
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.PaymentMethods.objects.create(**kwargs)
            return InsertPaymentMethods(payment_methods=models.PaymentMethods.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertPaymentMethods(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdatePaymentMethods(graphene.Mutation):
    success = graphene.Boolean()
    payment_methods = graphene.Field(types.PaymentMethodsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updatePaymentMethods(id:"", name:"oravpauuqr", abbreviated:"ffzveewfts", isDeleted:true, addedBy:){
>                success
>                errors
>                paymentMethods   
        >            { 
                            >    id 
                            >    name 
                            >    abbreviated 
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
        
            kwargs['id'] = models.PaymentMethods.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.PaymentMethods.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdatePaymentMethods(payment_methods=models.PaymentMethods.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdatePaymentMethods(errors=error, success=False)
        