#Mutation test request
        
                
'''        
mutation{
        > createBeverageRackOwner(rack:, rackOwner:)
        
            {
                success
                errors
                beverageRackOwner   
                        { 
                                id 
                            rack 
                                {
                                    id
                                }
                             
                            rackOwner 
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
        
>    updateBeverageRackOwner(id:"", rack:, rackOwner:, isActive:false, isDeleted:true)
            {
                success
                errors
                beverageRackOwner   
                        { 
                                id 
                            rack 
                                {
>                                    id
                                }
                             
                            rackOwner 
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
        