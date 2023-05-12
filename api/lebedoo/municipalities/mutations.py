import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .municipalities.types import MunicipalitiesType, MunicipalitiesFilter 
# from .municipalities import queries as municipalities_queries, mutations as municipalities_mutations       
#    create_municipalities = municipalities_mutations.InsertMunicipalities.Field()
#    update_municipalities = municipalities_mutations.UpdateMunicipalities.Field()
#    municipalities_queries.MunicipalitiesQuery,


# 
# ********************* insertion class *********************
class InsertMunicipalities(graphene.Mutation):
    success = graphene.Boolean()
    municipalities = graphene.Field(types.MunicipalitiesType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        city = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createMunicipalities(name:"njimzftabm", city:)
        > {
>                success
>                errors
>                municipalities   
        >             { 
>                                id 
>                                name 
>                            city 
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
        
            kwargs['city'] = models.Cities.objects.get(id=kwargs['city'])
                    
            models.Municipalities.objects.create(**kwargs)
            return InsertMunicipalities(municipalities=models.Municipalities.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertMunicipalities(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateMunicipalities(graphene.Mutation):
    success = graphene.Boolean()
    municipalities = graphene.Field(types.MunicipalitiesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        city = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateMunicipalities(id:"", name:"shrcnyqjyc", city:, isActive:false, isDeleted:false){
>                success
>                errors
>                municipalities   
        >            { 
                            >    id 
                            >    name 
                            city 
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
        
            kwargs['id'] = models.Municipalities.objects.get(id=kwargs['id']).id
                    
            kwargs['city'] = models.Cities.objects.get(id=kwargs['city']).id
                    
            models.Municipalities.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateMunicipalities(municipalities=models.Municipalities.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateMunicipalities(errors=error, success=False)
        