import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .property.types import PropertyType, PropertyFilter 
# from .property import queries as property_queries, mutations as property_mutations       
#    create_property = property_mutations.InsertProperty.Field()
#    update_property = property_mutations.UpdateProperty.Field()
#    property_queries.PropertyQuery,


# 
# ********************* insertion class *********************
class InsertProperty(graphene.Mutation):
    success = graphene.Boolean()
    property = graphene.Field(types.PropertyType)
    errors = graphene.String()

    class Arguments:

        code = graphene.String()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createProperty(code:"gmgjkeuqww", addedBy:)
        > {
>                success
>                errors
>                property   
        >             { 
>                                id 
>                                code 
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
                    
            models.Property.objects.create(**kwargs)
            return InsertProperty(property=models.Property.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertProperty(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateProperty(graphene.Mutation):
    success = graphene.Boolean()
    property = graphene.Field(types.PropertyType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        code = graphene.String()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateProperty(id:"", code:"yrtfnjalht", isActive:false, isDeleted:false, addedBy:){
>                success
>                errors
>                property   
        >            { 
                            >    id 
                            >    code 
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
        
            kwargs['id'] = models.Property.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Property.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateProperty(property=models.Property.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateProperty(errors=error, success=False)
        