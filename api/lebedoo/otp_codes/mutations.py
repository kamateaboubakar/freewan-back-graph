import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .otp_codes.types import OtpCodesType, OtpCodesFilter 
# from .otp_codes import queries as otp_codes_queries, mutations as otp_codes_mutations       
#    create_otp_codes = otp_codes_mutations.InsertOtpCodes.Field()
#    update_otp_codes = otp_codes_mutations.UpdateOtpCodes.Field()
#    otp_codes_queries.OtpCodesQuery,


# 
# ********************* insertion class *********************
class InsertOtpCodes(graphene.Mutation):
    success = graphene.Boolean()
    otp_codes = graphene.Field(types.OtpCodesType)
    errors = graphene.String()

    class Arguments:

        otp_code = graphene.Int()
                    
        phone_number = graphene.String()
                    
        country_code = graphene.ID(required=True)
                    
        expiry_time = graphene.Int()
                    
        is_expired = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createOtpCodes(otpCode:23355, phoneNumber:"evpxyifwvy", countryCode:, expiryTime:25271, isExpired:true, addedBy:)
        > {
>                success
>                errors
>                otpCodes   
        >             { 
>                                id 
>                                otpCode 
>                                phoneNumber 
>                            countryCode 
>                                {
>                                    id
>                                } 
>                                expiryTime 
>                                isExpired 
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
        
            kwargs['country_code'] = models.Country.objects.get(id=kwargs['country_code'])
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.OtpCodes.objects.create(**kwargs)
            return InsertOtpCodes(otp_codes=models.OtpCodes.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertOtpCodes(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateOtpCodes(graphene.Mutation):
    success = graphene.Boolean()
    otp_codes = graphene.Field(types.OtpCodesType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        otp_code = graphene.Int()
                    
        phone_number = graphene.String()
                    
        country_code = graphene.ID(required=True)
                    
        expiry_time = graphene.Int()
                    
        is_expired = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateOtpCodes(id:"", otpCode:55692, phoneNumber:"fafxsmwrtu", countryCode:, expiryTime:14462, isExpired:false, addedBy:){
>                success
>                errors
>                otpCodes   
        >            { 
                            >    id 
                            >    otpCode 
                            >    phoneNumber 
                            countryCode 
                                {
>                                    id
                                } 
                            >    expiryTime 
                            >    isExpired 
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
        
            kwargs['id'] = models.OtpCodes.objects.get(id=kwargs['id']).id
                    
            kwargs['country_code'] = models.Country.objects.get(id=kwargs['country_code']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.OtpCodes.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateOtpCodes(otp_codes=models.OtpCodes.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateOtpCodes(errors=error, success=False)
        