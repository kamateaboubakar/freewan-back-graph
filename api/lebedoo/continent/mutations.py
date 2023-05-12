import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .continent.types import ContinentType, ContinentFilter 
# from .continent import queries as continent_queries, mutations as continent_mutations       
#    create_continent = continent_mutations.InsertContinent.Field()
#    update_continent = continent_mutations.UpdateContinent.Field()
#    continent_queries.ContinentQuery,


# 
# ********************* insertion class *********************
class InsertContinent(graphene.Mutation):
    success = graphene.Boolean()
    continent = graphene.Field(types.ContinentType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createContinent(name:"elqomkdzab",)
        > {
>                success
>                errors
>                continent   
        >             { 
>                                id 
>                                name 
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
        
            models.Continent.objects.create(**kwargs)
            return InsertContinent(continent=models.Continent.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertContinent(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateContinent(graphene.Mutation):
    success = graphene.Boolean()
    continent = graphene.Field(types.ContinentType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateContinent(id:"", name:"qhmxdyxqkl", isActive:false, isDeleted:true){
>                success
>                errors
>                continent   
        >            { 
                            >    id 
                            >    name 
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
        
            kwargs['id'] = models.Continent.objects.get(id=kwargs['id']).id
                    
            models.Continent.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateContinent(continent=models.Continent.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateContinent(errors=error, success=False)
        