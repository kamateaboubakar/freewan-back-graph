import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .sand_vendors.types import SandVendorsType, SandVendorsFilter 
# from .sand_vendors import queries as sand_vendors_queries, mutations as sand_vendors_mutations       
#    create_sand_vendors = sand_vendors_mutations.InsertSandVendors.Field()
#    update_sand_vendors = sand_vendors_mutations.UpdateSandVendors.Field()
#    sand_vendors_queries.SandVendorsQuery,


# 
# ********************* insertion class *********************
class InsertSandVendors(graphene.Mutation):
    success = graphene.Boolean()
    sand_vendors = graphene.Field(types.SandVendorsType)
    errors = graphene.String()

    class Arguments:

        sand_infos = graphene.ID(required=True)
                    
        sand_owner = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createSandVendors(sandInfos:, sandOwner:)
        > {
>                success
>                errors
>                sandVendors   
        >             { 
>                                id 
>                            sandInfos 
>                                {
>                                    id
>                                } 
>                            sandOwner 
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
        
            kwargs['sand_infos'] = models.SandInfos.objects.get(id=kwargs['sand_infos'])
                    
            kwargs['sand_owner'] = models.Users.objects.get(id=kwargs['sand_owner'])
                    
            models.SandVendors.objects.create(**kwargs)
            return InsertSandVendors(sand_vendors=models.SandVendors.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertSandVendors(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateSandVendors(graphene.Mutation):
    success = graphene.Boolean()
    sand_vendors = graphene.Field(types.SandVendorsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        sand_infos = graphene.ID(required=True)
                    
        sand_owner = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateSandVendors(id:"", sandInfos:, sandOwner:, isActive:false, isDeleted:true){
>                success
>                errors
>                sandVendors   
        >            { 
                            >    id 
                            sandInfos 
                                {
>                                    id
                                } 
                            sandOwner 
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
        
            kwargs['id'] = models.SandVendors.objects.get(id=kwargs['id']).id
                    
            kwargs['sand_infos'] = models.SandInfos.objects.get(id=kwargs['sand_infos']).id
                    
            kwargs['sand_owner'] = models.Users.objects.get(id=kwargs['sand_owner']).id
                    
            models.SandVendors.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateSandVendors(sand_vendors=models.SandVendors.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateSandVendors(errors=error, success=False)
        