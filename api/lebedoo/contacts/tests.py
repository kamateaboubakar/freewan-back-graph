#Mutation test request
        
                
'''        
mutation{
        > createContacts(users:, country:, phoneNumber:"fiqwkmjqfs")
        
            {
                success
                errors
                contacts   
                        { 
                                id 
                            users 
                                {
                                    id
                                }
                             
                            country 
                                {
                                    id
                                }
                             
                                phoneNumber 
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
        
>    updateContacts(id:"", users:, country:, phoneNumber:"zstilkrgwu", isActive:false, isDeleted:false)
            {
                success
                errors
                contacts   
                        { 
                                id 
                            users 
                                {
>                                    id
                                }
                             
                            country 
                                {
>                                    id
                                }
                             
                                phoneNumber 
                                isActive 
                                isDeleted 
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        