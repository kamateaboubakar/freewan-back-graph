import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .sand_infos.types import SandInfosType, SandInfosFilter 
# from .sand_infos import queries as sand_infos_queries, mutations as sand_infos_mutations       
#    create_sand_infos = sand_infos_mutations.InsertSandInfos.Field()
#    update_sand_infos = sand_infos_mutations.UpdateSandInfos.Field()
#    sand_infos_queries.SandInfosQuery,


# 
# ********************* insertion class *********************
class InsertSandInfos(graphene.Mutation):
    success = graphene.Boolean()
    sand_infos = graphene.Field(types.SandInfosType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        details = graphene.JSONString(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createSandInfos(name:"xlozdagghw", details:""{"key":"value"}"", addedBy:)
        > {
>                success
>                errors
>                sandInfos   
        >             { 
>                                id 
>                                name 
>                                details 
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
        
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.SandInfos.objects.create(**kwargs)
            return InsertSandInfos(sand_infos=models.SandInfos.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertSandInfos(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateSandInfos(graphene.Mutation):
    success = graphene.Boolean()
    sand_infos = graphene.Field(types.SandInfosType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        details = graphene.JSONString()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateSandInfos(id:"", name:"mjnaokbmne", details:{"key":"value"}, isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                sandInfos   
        >            { 
                            >    id 
                            >    name 
                            >    details 
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
        
            kwargs['id'] = models.SandInfos.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.SandInfos.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateSandInfos(sand_infos=models.SandInfos.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateSandInfos(errors=error, success=False)
        