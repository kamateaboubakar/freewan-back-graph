#Mutation test request
        
                
'''        
mutation{
        > createRolesPrivileges(privilege:, role:)
        
            {
                success
                errors
                rolesPrivileges   
                        { 
                                id 
                            privilege 
                                {
                                    id
                                }
                             
                            role 
                                {
                                    id
                                }
                            
        }
    }
}
        
'''        
        #Mutation test request
        
        
#*****************************************************Mutation test request************************************************        
        
'''        
mutation{
        
>    updateRolesPrivileges(id:"", privilege:, role:)
            {
                success
                errors
                rolesPrivileges   
                        { 
                                id 
                            privilege 
                                {
>                                    id
                                }
                             
                            role 
                                {
>                                    id
                                }
                            
        }
    }
}
        
'''        
        