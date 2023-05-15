#Mutation test request
        
                
'''        
mutation{
        > createOtpCodes(otpCode:23355, phoneNumber:"evpxyifwvy", countryCode:, expiryTime:25271, isExpired:true, addedBy:)
        
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
        
>    updateOtpCodes(id:"", otpCode:55692, phoneNumber:"fafxsmwrtu", countryCode:, expiryTime:14462, isExpired:false, addedBy:)
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
        