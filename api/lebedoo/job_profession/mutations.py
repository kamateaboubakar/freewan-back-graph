import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .job_profession.types import JobProfessionType, JobProfessionFilter 
# from .job_profession import queries as job_profession_queries, mutations as job_profession_mutations       
#    create_job_profession = job_profession_mutations.InsertJobProfession.Field()
#    update_job_profession = job_profession_mutations.UpdateJobProfession.Field()
#    job_profession_queries.JobProfessionQuery,


# 
# ********************* insertion class *********************
class InsertJobProfession(graphene.Mutation):
    success = graphene.Boolean()
    job_profession = graphene.Field(types.JobProfessionType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createJobProfession(name:"rkpzbclhye",)
        > {
>                success
>                errors
>                jobProfession   
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
        
            models.JobProfession.objects.create(**kwargs)
            return InsertJobProfession(job_profession=models.JobProfession.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertJobProfession(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateJobProfession(graphene.Mutation):
    success = graphene.Boolean()
    job_profession = graphene.Field(types.JobProfessionType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateJobProfession(id:"", name:"pcuoizakvm", isDeleted:false){
>                success
>                errors
>                jobProfession   
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
        
            kwargs['id'] = models.JobProfession.objects.get(id=kwargs['id']).id
                    
            models.JobProfession.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateJobProfession(job_profession=models.JobProfession.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateJobProfession(errors=error, success=False)
        