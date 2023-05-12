#Mutation test request
        
                
'''        
mutation{
        > createRegion(name:"etvavenntu", country:)
        
            {
                success
                errors
                region   
                        { 
                                id 
                                name 
                            country 
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
        
>    updateRegion(id:"", name:"jatokuithl", country:, isActive:false, isDeleted:false)
            {
                success
                errors
                region   
                        { 
                                id 
                                name 
                            country 
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
        