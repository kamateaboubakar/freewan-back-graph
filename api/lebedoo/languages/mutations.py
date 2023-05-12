import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .languages.types import LanguagesType, LanguagesFilter 
# from .languages import queries as languages_queries, mutations as languages_mutations       
#    create_languages = languages_mutations.InsertLanguages.Field()
#    update_languages = languages_mutations.UpdateLanguages.Field()
#    languages_queries.LanguagesQuery,


# 
# ********************* insertion class *********************
class InsertLanguages(graphene.Mutation):
    success = graphene.Boolean()
    languages = graphene.Field(types.LanguagesType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
    class Meta:
        description = '''        
> mutation{
        > createLanguages(name:"cbtzwcwexm", abbreviated:"yinrchhdqx")
        > {
>                success
>                errors
>                languages   
        >             { 
>                                id 
>                                name 
>                                abbreviated 
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
        
            models.Languages.objects.create(**kwargs)
            return InsertLanguages(languages=models.Languages.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertLanguages(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateLanguages(graphene.Mutation):
    success = graphene.Boolean()
    languages = graphene.Field(types.LanguagesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateLanguages(id:"", name:"bdhszizesj", abbreviated:"mmqmltcpzs", isActive:true, isDeleted:false){
>                success
>                errors
>                languages   
        >            { 
                            >    id 
                            >    name 
                            >    abbreviated 
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
        
            kwargs['id'] = models.Languages.objects.get(id=kwargs['id']).id
                    
            models.Languages.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateLanguages(languages=models.Languages.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateLanguages(errors=error, success=False)
        