#Mutation test request
        
                
'''        
mutation{
        > createUserPrivileges(name:"jahuslinpv",)
        
            {
                success
                errors
                userPrivileges   
                        { 
                                id 
                                name 
                                isActive 
                                isDeleted 
                                createdAt 
                                updatedAt
        }
    }
}
        
'''        
        #Mutation test request
        
        
#*****************************************************Mutation test request************************************************        
        
'''        
mutation{
        
>    updateUserPrivileges(id:"", name:"dnpfnyrsxr", isActive:false, isDeleted:true)
            {
                success
                errors
                userPrivileges   
                        { 
                                id 
                                name 
                                isActive 
                                isDeleted 
                                createdAt 
                                updatedAt
        }
    }
}
        
'''        
        