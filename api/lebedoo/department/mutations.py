import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .department.types import DepartmentType, DepartmentFilter 
# from .department import queries as department_queries, mutations as department_mutations       
#    create_department = department_mutations.InsertDepartment.Field()
#    update_department = department_mutations.UpdateDepartment.Field()
#    department_queries.DepartmentQuery,


# 
# ********************* insertion class *********************
class InsertDepartment(graphene.Mutation):
    success = graphene.Boolean()
    department = graphene.Field(types.DepartmentType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        region = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createDepartment(name:"ospibtfagd", region:)
        > {
>                success
>                errors
>                department   
        >             { 
>                                id 
>                                name 
>                            region 
>                                {
>                                    id
>                                } 
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
        
            kwargs['region'] = models.Region.objects.get(id=kwargs['region'])
                    
            models.Department.objects.create(**kwargs)
            return InsertDepartment(department=models.Department.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertDepartment(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateDepartment(graphene.Mutation):
    success = graphene.Boolean()
    department = graphene.Field(types.DepartmentType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        region = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateDepartment(id:"", name:"lcmgfjqamm", region:, isActive:true, isDeleted:true){
>                success
>                errors
>                department   
        >            { 
                            >    id 
                            >    name 
                            region 
                                {
>                                    id
                                } 
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
        
            kwargs['id'] = models.Department.objects.get(id=kwargs['id']).id
                    
            kwargs['region'] = models.Region.objects.get(id=kwargs['region']).id
                    
            models.Department.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateDepartment(department=models.Department.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateDepartment(errors=error, success=False)
        