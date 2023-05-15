import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .users_security_questions.types import UsersSecurityQuestionsType, UsersSecurityQuestionsFilter 
# from .users_security_questions import queries as users_security_questions_queries, mutations as users_security_questions_mutations       
#    create_users_security_questions = users_security_questions_mutations.InsertUsersSecurityQuestions.Field()
#    update_users_security_questions = users_security_questions_mutations.UpdateUsersSecurityQuestions.Field()
#    users_security_questions_queries.UsersSecurityQuestionsQuery,


# 
# ********************* insertion class *********************
class InsertUsersSecurityQuestions(graphene.Mutation):
    success = graphene.Boolean()
    users_security_questions = graphene.Field(types.UsersSecurityQuestionsType)
    errors = graphene.String()

    class Arguments:

        questions = graphene.ID(required=True)
                    
        question_answers = graphene.String()
                    
        user = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createUsersSecurityQuestions(questions:, questionAnswers:"pbhdgtvold", user:)
        > {
>                success
>                errors
>                usersSecurityQuestions   
        >             { 
>                                id 
>                            questions 
>                                {
>                                    id
>                                } 
>                                questionAnswers 
>                            user 
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
        
            kwargs['questions'] = models.SecurityQuestions.objects.get(id=kwargs['questions'])
                    
            kwargs['user'] = models.Users.objects.get(id=kwargs['user'])
                    
            models.UsersSecurityQuestions.objects.create(**kwargs)
            return InsertUsersSecurityQuestions(users_security_questions=models.UsersSecurityQuestions.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertUsersSecurityQuestions(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateUsersSecurityQuestions(graphene.Mutation):
    success = graphene.Boolean()
    users_security_questions = graphene.Field(types.UsersSecurityQuestionsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        questions = graphene.ID(required=True)
                    
        question_answers = graphene.String()
                    
        user = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateUsersSecurityQuestions(id:"", questions:, questionAnswers:"payusivkxe", user:){
>                success
>                errors
>                usersSecurityQuestions   
        >            { 
                            >    id 
                            questions 
                                {
>                                    id
                                } 
                            >    questionAnswers 
                            user 
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
        
            kwargs['id'] = models.UsersSecurityQuestions.objects.get(id=kwargs['id']).id
                    
            kwargs['questions'] = models.SecurityQuestions.objects.get(id=kwargs['questions']).id
                    
            kwargs['user'] = models.Users.objects.get(id=kwargs['user']).id
                    
            models.UsersSecurityQuestions.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateUsersSecurityQuestions(users_security_questions=models.UsersSecurityQuestions.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateUsersSecurityQuestions(errors=error, success=False)
        