import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .years.types import YearsType, YearsFilter 
# from .years import queries as years_queries, mutations as years_mutations       
#    create_years = years_mutations.InsertYears.Field()
#    update_years = years_mutations.UpdateYears.Field()
#    years_queries.YearsQuery,


# 
# ********************* insertion class *********************
class InsertYears(graphene.Mutation):
    success = graphene.Boolean()
    years = graphene.Field(types.YearsType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createYears(name:"bljfezukbb", abbreviated:"spnupdwiin", addedBy:)
        > {
>                success
>                errors
>                years   
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
                    
            models.Years.objects.create(**kwargs)
            return InsertYears(years=models.Years.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertYears(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateYears(graphene.Mutation):
    success = graphene.Boolean()
    years = graphene.Field(types.YearsType)
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
        
>    updateYears(id:"", name:"yynbhaxcvh", abbreviated:"plhpbqqkmj", isDeleted:false, addedBy:){
>                success
>                errors
>                years   
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
        
            kwargs['id'] = models.Years.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Years.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateYears(years=models.Years.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateYears(errors=error, success=False)
        