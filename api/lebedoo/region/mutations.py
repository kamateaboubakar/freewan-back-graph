import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .region.types import RegionType, RegionFilter 
# from .region import queries as region_queries, mutations as region_mutations       
#    create_region = region_mutations.InsertRegion.Field()
#    update_region = region_mutations.UpdateRegion.Field()
#    region_queries.RegionQuery,


# 
# ********************* insertion class *********************
class InsertRegion(graphene.Mutation):
    success = graphene.Boolean()
    region = graphene.Field(types.RegionType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        country = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createRegion(name:"etvavenntu", country:)
        > {
>                success
>                errors
>                region   
        >             { 
>                                id 
>                                name 
>                            country 
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
        
            kwargs['country'] = models.Country.objects.get(id=kwargs['country'])
                    
            models.Region.objects.create(**kwargs)
            return InsertRegion(region=models.Region.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertRegion(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateRegion(graphene.Mutation):
    success = graphene.Boolean()
    region = graphene.Field(types.RegionType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        country = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateRegion(id:"", name:"jatokuithl", country:, isActive:false, isDeleted:false){
>                success
>                errors
>                region   
        >            { 
                            >    id 
                            >    name 
                            country 
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
        
            kwargs['id'] = models.Region.objects.get(id=kwargs['id']).id
                    
            kwargs['country'] = models.Country.objects.get(id=kwargs['country']).id
                    
            models.Region.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateRegion(region=models.Region.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateRegion(errors=error, success=False)
        