#Mutation test request
        
                
'''        
mutation{
        > createPropertyTenants(property:, propertyTenant:)
        
            {
                success
                errors
                propertyTenants   
                        { 
                                id 
                            property 
                                {
                                    id
                                }
                             
                            propertyTenant 
                                {
                                    id
                                }
                             
                                isActive 
                                isDeleted
        }
    }
}
        
'''        
        #Mutation test request
        
        
#*****************************************************Mutation test request************************************************        
        
'''        
mutation{
        
>    updatePropertyTenants(id:"", property:, propertyTenant:, isActive:true, isDeleted:false)
            {
                success
                errors
                propertyTenants   
                        { 
                                id 
                            property 
                                {
>                                    id
                                }
                             
                            propertyTenant 
                                {
>                                    id
                                }
                             
                                isActive 
                                isDeleted
        }
    }
}
        
'''        
        