#Mutation test request
        
                
'''        
mutation{
        > createBeverageRackPayments(amount:0.6210780835589742, paymentsDetails:""{"key":"value"}"", rack:, rackOwner:, rackBuyer:, addedBy:)
        
            {
                success
                errors
                beverageRackPayments   
                        { 
                                id 
                                amount 
                                paymentsDetails 
                            rack 
                                {
                                    id
                                }
                             
                            rackOwner 
                                {
                                    id
                                }
                             
                            rackBuyer 
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
        
>    updateBeverageRackPayments(id:"", amount:0.9084881233940553, paymentsDetails:{"key":"value"}, rack:, rackOwner:, rackBuyer:, isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                beverageRackPayments   
                        { 
                                id 
                                amount 
                                paymentsDetails 
                            rack 
                                {
>                                    id
                                }
                             
                            rackOwner 
                                {
>                                    id
                                }
                             
                            rackBuyer 
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
        