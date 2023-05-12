#Mutation test request
        
                
'''        
mutation{
        > createSandVendors(sandInfos:, sandOwner:)
        
            {
                success
                errors
                sandVendors   
                        { 
                                id 
                            sandInfos 
                                {
                                    id
                                }
                             
                            sandOwner 
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
        
>    updateSandVendors(id:"", sandInfos:, sandOwner:, isActive:false, isDeleted:true)
            {
                success
                errors
                sandVendors   
                        { 
                                id 
                            sandInfos 
                                {
>                                    id
                                }
                             
                            sandOwner 
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
        