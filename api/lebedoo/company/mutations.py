import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .company.types import CompanyType, CompanyFilter 
# from .company import queries as company_queries, mutations as company_mutations       
#    create_company = company_mutations.InsertCompany.Field()
#    update_company = company_mutations.UpdateCompany.Field()
#    company_queries.CompanyQuery,


# 
# ********************* insertion class *********************
class InsertCompany(graphene.Mutation):
    success = graphene.Boolean()
    company = graphene.Field(types.CompanyType)
    errors = graphene.String()

    class Arguments:

        name = graphene.String()
                    
        legal_form = graphene.String()
                    
        logo = graphene.String()
                    
        address = graphene.JSONString(required=True)
                    
        contact = graphene.JSONString(required=True)
                    
        area = graphene.JSONString(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createCompany(name:"cddcgrxfaf", legalForm:"ehsqmntfmz", logo:"fxxeupvqpj", address:""{"key":"value"}"", contact:""{"key":"value"}"", area:""{"key":"value"}"", addedBy:)
        > {
>                success
>                errors
>                company   
        >             { 
>                                id 
>                                name 
>                                legalForm 
>                                logo 
>                                address 
>                                contact 
>                                area 
>                            addedBy 
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
        
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.Company.objects.create(**kwargs)
            return InsertCompany(company=models.Company.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertCompany(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateCompany(graphene.Mutation):
    success = graphene.Boolean()
    company = graphene.Field(types.CompanyType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        name = graphene.String()
                    
        legal_form = graphene.String()
                    
        logo = graphene.String()
                    
        address = graphene.JSONString()
                    
        contact = graphene.JSONString()
                    
        area = graphene.JSONString()
                    
        added_by = graphene.ID(required=True)
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateCompany(id:"", name:"svtdtrqlfi", legalForm:"przomchllp", logo:"kqmqgiuoml", address:{"key":"value"}, contact:{"key":"value"}, area:{"key":"value"}, addedBy:, isActive:false, isDeleted:false){
>                success
>                errors
>                company   
        >            { 
                            >    id 
                            >    name 
                            >    legalForm 
                            >    logo 
                            >    address 
                            >    contact 
                            >    area 
                            addedBy 
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
        
            kwargs['id'] = models.Company.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.Company.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateCompany(company=models.Company.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateCompany(errors=error, success=False)
        