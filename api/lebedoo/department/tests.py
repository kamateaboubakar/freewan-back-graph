#Mutation test request
        
                
'''        
mutation{
        > createDepartment(name:"ospibtfagd", region:)
        
            {
                success
                errors
                department   
                        { 
                                id 
                                name 
                            region 
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
        
>    updateDepartment(id:"", name:"lcmgfjqamm", region:, isActive:true, isDeleted:true)
            {
                success
                errors
                department   
                        { 
                                id 
                                name 
                            region 
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
        