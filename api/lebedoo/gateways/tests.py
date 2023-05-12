#Mutation test request
        
                
'''        
mutation{
        > createGateways(addedBy:,)
        
            {
                success
                errors
                gateways   
                        { 
                                id 
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
        
>    updateGateways(id:"", isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                gateways   
                        { 
                                id 
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
        