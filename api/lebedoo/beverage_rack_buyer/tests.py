#Mutation test request
        
                
'''        
mutation{
        > createBeverageRackBuyer(rack:, rackBuyer:)
        
            {
                success
                errors
                beverageRackBuyer   
                        { 
                                id 
                            rack 
                                {
                                    id
                                }
                             
                            rackBuyer 
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
        
>    updateBeverageRackBuyer(id:"", rack:, rackBuyer:, isActive:false, isDeleted:false)
            {
                success
                errors
                beverageRackBuyer   
                        { 
                                id 
                            rack 
                                {
>                                    id
                                }
                             
                            rackBuyer 
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
        