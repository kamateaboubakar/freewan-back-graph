#Mutation test request
        
                
'''        
mutation{
        > createMunicipalities(name:"njimzftabm", city:)
        
            {
                success
                errors
                municipalities   
                        { 
                                id 
                                name 
                            city 
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
        
>    updateMunicipalities(id:"", name:"shrcnyqjyc", city:, isActive:false, isDeleted:false)
            {
                success
                errors
                municipalities   
                        { 
                                id 
                                name 
                            city 
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
        