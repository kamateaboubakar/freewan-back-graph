#Mutation test request
        
                
'''        
mutation{
        > createCountry(name:"vitfnmopux", ext:67118, code:"hswppeznnq", continent:)
        
            {
                success
                errors
                country   
                        { 
                                id 
                                name 
                                ext 
                                code 
                            continent 
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
        
>    updateCountry(id:"", name:"hvtopkhqlk", ext:26923, code:"vizujxvqpg", continent:, isActive:false, isDeleted:true)
            {
                success
                errors
                country   
                        { 
                                id 
                                name 
                                ext 
                                code 
                            continent 
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
        