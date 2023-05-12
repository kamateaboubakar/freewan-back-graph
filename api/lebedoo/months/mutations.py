import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .months.types import MonthsType, MonthsFilter 
# from .months import queries as months_queries, mutations as months_mutations       
#    create_months = months_mutations.InsertMonths.Field()
#    update_months = months_mutations.UpdateMonths.Field()
#    months_queries.MonthsQuery,


# 
# ********************* insertion class *********************
class InsertMonths(graphene.Mutation):
    success = graphene.Boolean()
    months = graphene.Field(types.MonthsType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        abbreviated = graphene.String()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createMonths(name:"mkfbjuwlha", abbreviated:"szlrgbbiuj", addedBy:)
        > {
>                success
>                errors
>                months   
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
                    
            models.Months.objects.create(**kwargs)
            return InsertMonths(months=models.Months.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertMonths(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateMonths(graphene.Mutation):
    success = graphene.Boolean()
    months = graphene.Field(types.MonthsType)
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
        
>    updateMonths(id:"", name:"tdgroaaxgj", abbreviated:"bqikbmoqdb", isDeleted:false, addedBy:){
>                success
>                errors
>                months   
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
        
            kwargs['id'] = models.Months.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Months.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateMonths(months=models.Months.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateMonths(errors=error, success=False)
        