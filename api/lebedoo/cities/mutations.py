import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .cities.types import CitiesType, CitiesFilter 
# from .cities import queries as cities_queries, mutations as cities_mutations       
#    create_cities = cities_mutations.InsertCities.Field()
#    update_cities = cities_mutations.UpdateCities.Field()
#    cities_queries.CitiesQuery,


# 
# ********************* insertion class *********************
class InsertCities(graphene.Mutation):
    success = graphene.Boolean()
    cities = graphene.Field(types.CitiesType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        department = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createCities(name:"xlpexyeuph", department:)
        > {
>                success
>                errors
>                cities   
        >             { 
>                                id 
>                                name 
>                            department 
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
        
            kwargs['department'] = models.Department.objects.get(id=kwargs['department'])
                    
            models.Cities.objects.create(**kwargs)
            return InsertCities(cities=models.Cities.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertCities(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateCities(graphene.Mutation):
    success = graphene.Boolean()
    cities = graphene.Field(types.CitiesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        department = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateCities(id:"", name:"vgnmvrrdyu", department:, isActive:false, isDeleted:false){
>                success
>                errors
>                cities   
        >            { 
                            >    id 
                            >    name 
                            department 
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
        
            kwargs['id'] = models.Cities.objects.get(id=kwargs['id']).id
                    
            kwargs['department'] = models.Department.objects.get(id=kwargs['department']).id
                    
            models.Cities.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateCities(cities=models.Cities.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateCities(errors=error, success=False)
        