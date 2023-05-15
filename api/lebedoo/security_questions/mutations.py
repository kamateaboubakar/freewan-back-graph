import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .security_questions.types import SecurityQuestionsType, SecurityQuestionsFilter 
# from .security_questions import queries as security_questions_queries, mutations as security_questions_mutations       
#    create_security_questions = security_questions_mutations.InsertSecurityQuestions.Field()
#    update_security_questions = security_questions_mutations.UpdateSecurityQuestions.Field()
#    security_questions_queries.SecurityQuestionsQuery,


# 
# ********************* insertion class *********************
class InsertSecurityQuestions(graphene.Mutation):
    success = graphene.Boolean()
    security_questions = graphene.Field(types.SecurityQuestionsType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createSecurityQuestions(name:"pgfwujubrj",)
        > {
>                success
>                errors
>                securityQuestions   
        >             { 
>                                id 
>                                name 
>                                createdDate 
>                                updatedDate
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            models.SecurityQuestions.objects.create(**kwargs)
            return InsertSecurityQuestions(security_questions=models.SecurityQuestions.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertSecurityQuestions(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateSecurityQuestions(graphene.Mutation):
    success = graphene.Boolean()
    security_questions = graphene.Field(types.SecurityQuestionsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateSecurityQuestions(id:"", name:"rngkbmbeph"){
>                success
>                errors
>                securityQuestions   
        >            { 
                            >    id 
                            >    name 
                            >    createdDate 
                            >    updatedDate
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.SecurityQuestions.objects.get(id=kwargs['id']).id
                    
            models.SecurityQuestions.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateSecurityQuestions(security_questions=models.SecurityQuestions.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateSecurityQuestions(errors=error, success=False)
        