import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .gateways.types import GatewaysType, GatewaysFilter 
# from .gateways import queries as gateways_queries, mutations as gateways_mutations       
#    create_gateways = gateways_mutations.InsertGateways.Field()
#    update_gateways = gateways_mutations.UpdateGateways.Field()
#    gateways_queries.GatewaysQuery,


# 
# ********************* insertion class *********************
class InsertGateways(graphene.Mutation):
    success = graphene.Boolean()
    gateways = graphene.Field(types.GatewaysType)
    errors = graphene.String()

    class Arguments:

        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createGateways(addedBy:,)
        > {
>                success
>                errors
>                gateways   
        >             { 
>                                id 
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
                    
            models.Gateways.objects.create(**kwargs)
            return InsertGateways(gateways=models.Gateways.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertGateways(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateGateways(graphene.Mutation):
    success = graphene.Boolean()
    gateways = graphene.Field(types.GatewaysType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateGateways(id:"", isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                gateways   
        >            { 
                            >    id 
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
        
            kwargs['id'] = models.Gateways.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Gateways.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateGateways(gateways=models.Gateways.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateGateways(errors=error, success=False)
        