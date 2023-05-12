#Mutation test request
        
                
'''        
mutation{
        > createCurrencies(name:"lsffqgguwe", abbreviated:"opdrsivbkp", addedBy:)
        
            {
                success
                errors
                currencies   
                        { 
                                id 
                                name 
                                abbreviated 
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
        
>    updateCurrencies(id:"", name:"bodahqpxrh", abbreviated:"lrujvyvusu", isDeleted:true, addedBy:)
            {
                success
                errors
                currencies   
                        { 
                                id 
                                name 
                                abbreviated 
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
        