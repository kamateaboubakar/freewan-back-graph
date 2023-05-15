#Mutation test request
        
                
'''        
mutation{
        > createUsers(id:"", username:"fdthwbkxsh", email:"szcqvowsso", phoneNumber:"qphcdazklr", countryCode:, firstName:"jcdkjylhvn", lastName:"eadkyxuvor", privileges:"""{"role":"state"}""", isAdmin:true, isFreelancer:true, isClient:false)
        
            {
                success
                errors
                users   
                        { 
                                id 
                                username 
                                email 
                                phoneNumber 
                            countryCode 
                                {
                                    id
                                }
                             
                                firstName 
                                lastName 
                                privileges 
                                isAdmin 
                                isFreelancer 
                                isClient 
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
        
>    updateUsers(id:"", username:"bqrrdpxluw", email:"uoivvlwoym", phoneNumber:"jatszejjic", countryCode:, firstName:"vflxdsrvmo", lastName:"gystiasblv", privileges:{"role":"state"}, isAdmin:true, isFreelancer:true, isClient:true, isDeleted:false)
            {
                success
                errors
                users   
                        { 
                                id 
                                username 
                                email 
                                phoneNumber 
                            countryCode 
                                {
>                                    id
                                }
                             
                                firstName 
                                lastName 
                                privileges 
                                isAdmin 
                                isFreelancer 
                                isClient 
                                isDeleted 
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        