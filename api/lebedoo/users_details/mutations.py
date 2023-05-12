import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .users_details.types import UsersDetailsType, UsersDetailsFilter 
# from .users_details import queries as users_details_queries, mutations as users_details_mutations       
#    create_users_details = users_details_mutations.InsertUsersDetails.Field()
#    update_users_details = users_details_mutations.UpdateUsersDetails.Field()
#    users_details_queries.UsersDetailsQuery,


# 
# ********************* insertion class *********************
class InsertUsersDetails(graphene.Mutation):
    success = graphene.Boolean()
    users_details = graphene.Field(types.UsersDetailsType)
    errors = graphene.String()

    class Arguments:

        user = graphene.ID(required=True)
                    
        gender = graphene.String()
                    
        civil_title = graphene.String()
                    
        dob = graphene.Date()
                    
        image = graphene.String()
                    
        description = graphene.String()
                    
        company = graphene.ID(required=True)
                    
        job_profession = graphene.ID(required=True)
                    
        job_function = graphene.ID(required=True)
                    
        address = graphene.JSONString(required=True)
                    
        contacts = graphene.JSONString(required=True)
                    
        languages = graphene.JSONString(required=True)
                    
        skills = graphene.JSONString(required=True)
                    
        experiences = graphene.JSONString(required=True)
                    
        links = graphene.JSONString(required=True)
                    
        degrees = graphene.JSONString(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createUsersDetails(user:, gender:"tfhyeuxtxj", civilTitle:"vneyofxhzs", dob:"2023-04-03", image:"wkajvgodji", description:"xauhdmvore", company:, jobProfession:, jobFunction:, address:""{"key":"value"}"", contacts:""{"key":"value"}"", languages:""{"key":"value"}"", skills:""{"key":"value"}"", experiences:""{"key":"value"}"", links:""{"key":"value"}"", degrees:""{"key":"value"}"")
        > {
>                success
>                errors
>                usersDetails   
        >             { 
>                                id 
>                            user 
>                                {
>                                    id
>                                } 
>                                gender 
>                                civilTitle 
>                                dob 
>                                image 
>                                description 
>                            company 
>                                {
>                                    id
>                                } 
>                            jobProfession 
>                                {
>                                    id
>                                } 
>                            jobFunction 
>                                {
>                                    id
>                                } 
>                                address 
>                                contacts 
>                                languages 
>                                skills 
>                                experiences 
>                                links 
>                                degrees
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['user'] = models.Users.objects.get(id=kwargs['user'])
                    
            kwargs['company'] = models.Company.objects.get(id=kwargs['company'])
                    
            kwargs['job_profession'] = models.JobProfession.objects.get(id=kwargs['job_profession'])
                    
            kwargs['job_function'] = models.JobFunction.objects.get(id=kwargs['job_function'])
                    
            models.UsersDetails.objects.create(**kwargs)
            return InsertUsersDetails(users_details=models.UsersDetails.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertUsersDetails(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateUsersDetails(graphene.Mutation):
    success = graphene.Boolean()
    users_details = graphene.Field(types.UsersDetailsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        user = graphene.ID(required=True)
                    
        gender = graphene.String()
                    
        civil_title = graphene.String()
                    
        dob = graphene.Date()
                    
        image = graphene.String()
                    
        description = graphene.String()
                    
        company = graphene.ID(required=True)
                    
        job_profession = graphene.ID(required=True)
                    
        job_function = graphene.ID(required=True)
                    
        address = graphene.JSONString()
                    
        contacts = graphene.JSONString()
                    
        languages = graphene.JSONString()
                    
        skills = graphene.JSONString()
                    
        experiences = graphene.JSONString()
                    
        links = graphene.JSONString()
                    
        degrees = graphene.JSONString()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateUsersDetails(id:"", user:, gender:"nalwfucdav", civilTitle:"xzkpmgabcb", dob:"2022-01-17", image:"mnfvjobumd", description:"pickwhiyds", company:, jobProfession:, jobFunction:, address:{"key":"value"}, contacts:{"key":"value"}, languages:{"key":"value"}, skills:{"key":"value"}, experiences:{"key":"value"}, links:{"key":"value"}, degrees:{"key":"value"}){
>                success
>                errors
>                usersDetails   
        >            { 
                            >    id 
                            user 
                                {
>                                    id
                                } 
                            >    gender 
                            >    civilTitle 
                            >    dob 
                            >    image 
                            >    description 
                            company 
                                {
>                                    id
                                } 
                            jobProfession 
                                {
>                                    id
                                } 
                            jobFunction 
                                {
>                                    id
                                } 
                            >    address 
                            >    contacts 
                            >    languages 
                            >    skills 
                            >    experiences 
                            >    links 
                            >    degrees
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.UsersDetails.objects.get(id=kwargs['id']).id
                    
            kwargs['user'] = models.Users.objects.get(id=kwargs['user']).id
                    
            kwargs['company'] = models.Company.objects.get(id=kwargs['company']).id
                    
            kwargs['job_profession'] = models.JobProfession.objects.get(id=kwargs['job_profession']).id
                    
            kwargs['job_function'] = models.JobFunction.objects.get(id=kwargs['job_function']).id
                    
            models.UsersDetails.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateUsersDetails(users_details=models.UsersDetails.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateUsersDetails(errors=error, success=False)
        