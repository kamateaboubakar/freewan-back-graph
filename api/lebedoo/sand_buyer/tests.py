#Mutation test request
        
                
'''        
mutation{
        > createSandBuyer(sandInfos:, sandBuyer:)
        
            {
                success
                errors
                sandBuyer   
                        { 
                                id 
                            sandInfos 
                                {
                                    id
                                }
                             
                            sandBuyer 
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
        
>    updateSandBuyer(id:"", sandInfos:, sandBuyer:, isActive:false, isDeleted:true)
            {
                success
                errors
                sandBuyer   
                        { 
                                id 
                            sandInfos 
                                {
>                                    id
                                }
                             
                            sandBuyer 
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
        