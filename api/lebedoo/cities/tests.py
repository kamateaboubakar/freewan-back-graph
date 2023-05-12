#Mutation test request
        
                
'''        
mutation{
        > createCities(name:"xlpexyeuph", department:)
        
            {
                success
                errors
                cities   
                        { 
                                id 
                                name 
                            department 
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
        
>    updateCities(id:"", name:"vgnmvrrdyu", department:, isActive:false, isDeleted:false)
            {
                success
                errors
                cities   
                        { 
                                id 
                                name 
                            department 
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
        