import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .sand_buyer.types import SandBuyerType, SandBuyerFilter 
# from .sand_buyer import queries as sand_buyer_queries, mutations as sand_buyer_mutations       
#    create_sand_buyer = sand_buyer_mutations.InsertSandBuyer.Field()
#    update_sand_buyer = sand_buyer_mutations.UpdateSandBuyer.Field()
#    sand_buyer_queries.SandBuyerQuery,


# 
# ********************* insertion class *********************
class InsertSandBuyer(graphene.Mutation):
    success = graphene.Boolean()
    sand_buyer = graphene.Field(types.SandBuyerType)
    errors = graphene.String()

    class Arguments:

        sand_infos = graphene.ID(required=True)
                    
        sand_buyer = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createSandBuyer(sandInfos:, sandBuyer:)
        > {
>                success
>                errors
>                sandBuyer   
        >             { 
>                                id 
>                            sandInfos 
>                                {
>                                    id
>                                } 
>                            sandBuyer 
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
                    
            kwargs['sand_buyer'] = models.Users.objects.get(id=kwargs['sand_buyer'])
                    
            models.SandBuyer.objects.create(**kwargs)
            return InsertSandBuyer(sand_buyer=models.SandBuyer.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertSandBuyer(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateSandBuyer(graphene.Mutation):
    success = graphene.Boolean()
    sand_buyer = graphene.Field(types.SandBuyerType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        sand_infos = graphene.ID(required=True)
                    
        sand_buyer = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateSandBuyer(id:"", sandInfos:, sandBuyer:, isActive:false, isDeleted:true){
>                success
>                errors
>                sandBuyer   
        >            { 
                            >    id 
                            sandInfos 
                                {
>                                    id
                                } 
                            sandBuyer 
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
        
            kwargs['id'] = models.SandBuyer.objects.get(id=kwargs['id']).id
                    
            kwargs['sand_infos'] = models.SandInfos.objects.get(id=kwargs['sand_infos']).id
                    
            kwargs['sand_buyer'] = models.Users.objects.get(id=kwargs['sand_buyer']).id
                    
            models.SandBuyer.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateSandBuyer(sand_buyer=models.SandBuyer.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateSandBuyer(errors=error, success=False)
        