import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .currencies.types import CurrenciesType, CurrenciesFilter 
# from .currencies import queries as currencies_queries, mutations as currencies_mutations       
#    create_currencies = currencies_mutations.InsertCurrencies.Field()
#    update_currencies = currencies_mutations.UpdateCurrencies.Field()
#    currencies_queries.CurrenciesQuery,


# 
# ********************* insertion class *********************
class InsertCurrencies(graphene.Mutation):
    success = graphene.Boolean()
    currencies = graphene.Field(types.CurrenciesType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createCurrencies(name:"lsffqgguwe", abbreviated:"opdrsivbkp", addedBy:)
        > {
>                success
>                errors
>                currencies   
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
                    
            models.Currencies.objects.create(**kwargs)
            return InsertCurrencies(currencies=models.Currencies.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertCurrencies(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateCurrencies(graphene.Mutation):
    success = graphene.Boolean()
    currencies = graphene.Field(types.CurrenciesType)
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
        
>    updateCurrencies(id:"", name:"bodahqpxrh", abbreviated:"lrujvyvusu", isDeleted:true, addedBy:){
>                success
>                errors
>                currencies   
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
        
            kwargs['id'] = models.Currencies.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Currencies.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateCurrencies(currencies=models.Currencies.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateCurrencies(errors=error, success=False)
        