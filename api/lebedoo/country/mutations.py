import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .country.types import CountryType, CountryFilter 
# from .country import queries as country_queries, mutations as country_mutations       
#    create_country = country_mutations.InsertCountry.Field()
#    update_country = country_mutations.UpdateCountry.Field()
#    country_queries.CountryQuery,


# 
# ********************* insertion class *********************
class InsertCountry(graphene.Mutation):
    success = graphene.Boolean()
    country = graphene.Field(types.CountryType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        ext = graphene.Int()
                    
        code = graphene.String()
                    
        continent = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createCountry(name:"vitfnmopux", ext:67118, code:"hswppeznnq", continent:)
        > {
>                success
>                errors
>                country   
        >             { 
>                                id 
>                                name 
>                                ext 
>                                code 
>                            continent 
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
        
            kwargs['continent'] = models.Continent.objects.get(id=kwargs['continent'])
                    
            models.Country.objects.create(**kwargs)
            return InsertCountry(country=models.Country.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertCountry(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateCountry(graphene.Mutation):
    success = graphene.Boolean()
    country = graphene.Field(types.CountryType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        ext = graphene.Int()
                    
        code = graphene.String()
                    
        continent = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateCountry(id:"", name:"hvtopkhqlk", ext:26923, code:"vizujxvqpg", continent:, isActive:false, isDeleted:true){
>                success
>                errors
>                country   
        >            { 
                            >    id 
                            >    name 
                            >    ext 
                            >    code 
                            continent 
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
        
            kwargs['id'] = models.Country.objects.get(id=kwargs['id']).id
                    
            kwargs['continent'] = models.Continent.objects.get(id=kwargs['continent']).id
                    
            models.Country.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateCountry(country=models.Country.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateCountry(errors=error, success=False)
        