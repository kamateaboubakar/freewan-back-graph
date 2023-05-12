import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .transactions.types import TransactionsType, TransactionsFilter 
# from .transactions import queries as transactions_queries, mutations as transactions_mutations       
#    create_transactions = transactions_mutations.InsertTransactions.Field()
#    update_transactions = transactions_mutations.UpdateTransactions.Field()
#    transactions_queries.TransactionsQuery,


# 
# ********************* insertion class *********************
class InsertTransactions(graphene.Mutation):
    success = graphene.Boolean()
    transactions = graphene.Field(types.TransactionsType)
    errors = graphene.String()

    class Arguments:

        amount = graphene.Float()
                    
        description = graphene.String()
                    
        gateway = graphene.ID(required=True)
                    
        payment_method = graphene.ID(required=True)
                    
        currency = graphene.ID(required=True)
                    
        status = graphene.ID(required=True)
                    
        metadata = graphene.JSONString(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createTransactions(amount:0.6634434999079923, description:"krohunyrtt", gateway:, paymentMethod:, currency:, status:, metadata:""{"key":"value"}"", addedBy:)
        > {
>                success
>                errors
>                transactions   
        >             { 
>                                id 
>                                amount 
>                                description 
>                            gateway 
>                                {
>                                    id
>                                } 
>                            paymentMethod 
>                                {
>                                    id
>                                } 
>                            currency 
>                                {
>                                    id
>                                } 
>                            status 
>                                {
>                                    id
>                                } 
>                                metadata 
>                            addedBy 
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
        
            kwargs['gateway'] = models.Gateways.objects.get(id=kwargs['gateway'])
                    
            kwargs['payment_method'] = models.PaymentMethods.objects.get(id=kwargs['payment_method'])
                    
            kwargs['currency'] = models.Currencies.objects.get(id=kwargs['currency'])
                    
            kwargs['status'] = models.Status.objects.get(id=kwargs['status'])
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.Transactions.objects.create(**kwargs)
            return InsertTransactions(transactions=models.Transactions.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertTransactions(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateTransactions(graphene.Mutation):
    success = graphene.Boolean()
    transactions = graphene.Field(types.TransactionsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        amount = graphene.Float()
                    
        description = graphene.String()
                    
        gateway = graphene.ID(required=True)
                    
        payment_method = graphene.ID(required=True)
                    
        currency = graphene.ID(required=True)
                    
        status = graphene.ID(required=True)
                    
        metadata = graphene.JSONString()
                    
        added_by = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateTransactions(id:"", amount:0.221014553849869, description:"insrepjpga", gateway:, paymentMethod:, currency:, status:, metadata:{"key":"value"}, addedBy:, isActive:false, isDeleted:false){
>                success
>                errors
>                transactions   
        >            { 
                            >    id 
                            >    amount 
                            >    description 
                            gateway 
                                {
>                                    id
                                } 
                            paymentMethod 
                                {
>                                    id
                                } 
                            currency 
                                {
>                                    id
                                } 
                            status 
                                {
>                                    id
                                } 
                            >    metadata 
                            addedBy 
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
        
            kwargs['id'] = models.Transactions.objects.get(id=kwargs['id']).id
                    
            kwargs['gateway'] = models.Gateways.objects.get(id=kwargs['gateway']).id
                    
            kwargs['payment_method'] = models.PaymentMethods.objects.get(id=kwargs['payment_method']).id
                    
            kwargs['currency'] = models.Currencies.objects.get(id=kwargs['currency']).id
                    
            kwargs['status'] = models.Status.objects.get(id=kwargs['status']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Transactions.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateTransactions(transactions=models.Transactions.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateTransactions(errors=error, success=False)
        