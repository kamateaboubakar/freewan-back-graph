#Mutation test request
        
                
'''        
mutation{
        > createProperty(code:"gmgjkeuqww", addedBy:)
        
            {
                success
                errors
                property   
                        { 
                                id 
                                code 
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
        
>    updateProperty(id:"", code:"yrtfnjalht", isActive:false, isDeleted:false, addedBy:)
            {
                success
                errors
                property   
                        { 
                                id 
                                code 
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
        