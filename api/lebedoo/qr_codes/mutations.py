import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .qr_codes.types import QrCodesType, QrCodesFilter 
# from .qr_codes import queries as qr_codes_queries, mutations as qr_codes_mutations       
#    create_qr_codes = qr_codes_mutations.InsertQrCodes.Field()
#    update_qr_codes = qr_codes_mutations.UpdateQrCodes.Field()
#    qr_codes_queries.QrCodesQuery,


# 
# ********************* insertion class *********************
class InsertQrCodes(graphene.Mutation):
    success = graphene.Boolean()
    qr_codes = graphene.Field(types.QrCodesType)
    errors = graphene.String()

    class Arguments:

        code = graphene.String()
                    
        details = graphene.JSONString(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createQrCodes(code:"cuqdglqgzn", details:""{"key":"value"}"", addedBy:)
        > {
>                success
>                errors
>                qrCodes   
        >             { 
>                                id 
>                                code 
>                                details 
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
                    
            models.QrCodes.objects.create(**kwargs)
            return InsertQrCodes(qr_codes=models.QrCodes.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertQrCodes(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateQrCodes(graphene.Mutation):
    success = graphene.Boolean()
    qr_codes = graphene.Field(types.QrCodesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        code = graphene.String()
                    
        details = graphene.JSONString()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateQrCodes(id:"", code:"qpajynuops", details:{"key":"value"}, isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                qrCodes   
        >            { 
                            >    id 
                            >    code 
                            >    details 
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
        
            kwargs['id'] = models.QrCodes.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.QrCodes.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateQrCodes(qr_codes=models.QrCodes.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateQrCodes(errors=error, success=False)
        