import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .status.types import StatusType, StatusFilter 
# from .status import queries as status_queries, mutations as status_mutations       
#    create_status = status_mutations.InsertStatus.Field()
#    update_status = status_mutations.UpdateStatus.Field()
#    status_queries.StatusQuery,


# 
# ********************* insertion class *********************
class InsertStatus(graphene.Mutation):
    success = graphene.Boolean()
    status = graphene.Field(types.StatusType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createStatus(name:"ptzlznljzc", abbreviated:"dvylkfyxkk", addedBy:)
        > {
>                success
>                errors
>                status   
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
                    
            models.Status.objects.create(**kwargs)
            return InsertStatus(status=models.Status.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertStatus(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateStatus(graphene.Mutation):
    success = graphene.Boolean()
    status = graphene.Field(types.StatusType)
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
        
>    updateStatus(id:"", name:"tfitfkzjvt", abbreviated:"ggyhchwqis", isDeleted:false, addedBy:){
>                success
>                errors
>                status   
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
        
            kwargs['id'] = models.Status.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Status.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateStatus(status=models.Status.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateStatus(errors=error, success=False)
        