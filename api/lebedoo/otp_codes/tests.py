#Mutation test request
        
                
'''        
mutation{
        > createOtpCodes(otpCode:"hksajptkon", phoneNumber:"pezmgjwdnm", countryCode:"1", expiryTime:95601, isExpired:true, addedBy:"RsE7zcjdIdud9vVdL3")
        
            {
                success
                errors
                otpCodes   
                        { 
                                id 
                                otpCode 
                                phoneNumber 
                            countryCode 
                                {
                                    id
                                }
                             
                                expiryTime 
                                isExpired 
                            addedBy 
                                {
                                    id
                                }
                             
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        #Mutation test request
        
        
#*****************************************************Mutation test request************************************************        
        
'''        
mutation{
        
>    updateOtpCodes(id:"", otpCode:"kyqvmffvhf", phoneNumber:"qcfhnltlcr", countryCode:, expiryTime:96698, isExpired:false, addedBy:)
            {
                success
                errors
                otpCodes   
                        { 
                                id 
                                otpCode 
                                phoneNumber 
                            countryCode 
                                {
>                                    id
                                }
                             
                                expiryTime 
                                isExpired 
                            addedBy 
                                {
>                                    id
                                }
                             
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        