#Mutation test request
        
                
'''        
mutation{
        > createUsers(id:"", username:"ujjujihzzb", email:"xdsbrsnbpo", firstName:"zffbwhfeds", lastName:"qnydlkmqfh", privileges:"""{"role":"state"}""", isAdmin:false, isFreelancer:false, isClient:false)
        
            {
                success
                errors
                users   
                        { 
                                id 
                                username 
                                email 
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
        
>    updateUsers(id:"", username:"tvdtuounwz", email:"atzotgbcxf", firstName:"orpxgnipjm", lastName:"zqrkfgzvaz", privileges:{"role":"state"}, isAdmin:false, isFreelancer:true, isClient:true, isDeleted:true)
            {
                success
                errors
                users   
                        { 
                                id 
                                username 
                                email 
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
        