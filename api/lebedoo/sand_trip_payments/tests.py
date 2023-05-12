#Mutation test request
        
                
'''        
mutation{
        > createSandTripPayments(sandTrip:, paymentsInfos:""{"key":"value"}"", sandTripOwners:, sandTripBuyer:, addedBy:)
        
            {
                success
                errors
                sandTripPayments   
                        { 
                                id 
                            sandTrip 
                                {
                                    id
                                }
                             
                                paymentsInfos 
                            sandTripOwners 
                                {
                                    id
                                }
                             
                            sandTripBuyer 
                                {
                                    id
                                }
                             
                                isActive 
                                isDeleted 
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
        
>    updateSandTripPayments(id:"", sandTrip:, paymentsInfos:{"key":"value"}, sandTripOwners:, sandTripBuyer:, isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                sandTripPayments   
                        { 
                                id 
                            sandTrip 
                                {
>                                    id
                                }
                             
                                paymentsInfos 
                            sandTripOwners 
                                {
>                                    id
                                }
                             
                            sandTripBuyer 
                                {
>                                    id
                                }
                             
                                isActive 
                                isDeleted 
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
        