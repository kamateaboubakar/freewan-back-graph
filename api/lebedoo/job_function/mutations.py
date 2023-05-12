import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .job_function.types import JobFunctionType, JobFunctionFilter 
# from .job_function import queries as job_function_queries, mutations as job_function_mutations       
#    create_job_function = job_function_mutations.InsertJobFunction.Field()
#    update_job_function = job_function_mutations.UpdateJobFunction.Field()
#    job_function_queries.JobFunctionQuery,


# 
# ********************* insertion class *********************
class InsertJobFunction(graphene.Mutation):
    success = graphene.Boolean()
    job_function = graphene.Field(types.JobFunctionType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createJobFunction(name:"mgabzciyfh",)
        > {
>                success
>                errors
>                jobFunction   
        >             { 
>                                id 
>                                name 
>                                isDeleted
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            models.JobFunction.objects.create(**kwargs)
            return InsertJobFunction(job_function=models.JobFunction.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertJobFunction(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateJobFunction(graphene.Mutation):
    success = graphene.Boolean()
    job_function = graphene.Field(types.JobFunctionType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateJobFunction(id:"", name:"ledyoiuxxe", isDeleted:false){
>                success
>                errors
>                jobFunction   
        >            { 
                            >    id 
                            >    name 
                            >    isDeleted
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.JobFunction.objects.get(id=kwargs['id']).id
                    
            models.JobFunction.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateJobFunction(job_function=models.JobFunction.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateJobFunction(errors=error, success=False)
        