#Mutation test request
        
                
'''        
mutation{
        > createTransactions(amount:0.6634434999079923, description:"krohunyrtt", gateway:, paymentMethod:, currency:, status:, metadata:""{"key":"value"}"", addedBy:)
        
            {
                success
                errors
                transactions   
                        { 
                                id 
                                amount 
                                description 
                            gateway 
                                {
                                    id
                                }
                             
                            paymentMethod 
                                {
                                    id
                                }
                             
                            currency 
                                {
                                    id
                                }
                             
                            status 
                                {
                                    id
                                }
                             
                                metadata 
                            addedBy 
                                {
                                    id
                                }
                             
                                isActive 
                                isDeleted 
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
        
>    updateTransactions(id:"", amount:0.221014553849869, description:"insrepjpga", gateway:, paymentMethod:, currency:, status:, metadata:{"key":"value"}, addedBy:, isActive:false, isDeleted:false)
            {
                success
                errors
                transactions   
                        { 
                                id 
                                amount 
                                description 
                            gateway 
                                {
>                                    id
                                }
                             
                            paymentMethod 
                                {
>                                    id
                                }
                             
                            currency 
                                {
>                                    id
                                }
                             
                            status 
                                {
>                                    id
                                }
                             
                                metadata 
                            addedBy 
                                {
>                                    id
                                }
                             
                                isActive 
                                isDeleted 
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        