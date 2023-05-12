#Mutation test request
        
                
'''        
mutation{
        > createPropertyOwners(property:, propertyOwner:)
        
            {
                success
                errors
                propertyOwners   
                        { 
                                id 
                            property 
                                {
                                    id
                                }
                             
                            propertyOwner 
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
        
>    updatePropertyOwners(id:"", property:, propertyOwner:, isActive:false, isDeleted:true)
            {
                success
                errors
                propertyOwners   
                        { 
                                id 
                            property 
                                {
>                                    id
                                }
                             
                            propertyOwner 
                                {
>                                    id
                                }
                             
                                isActive 
                                isDeleted
        }
    }
}
        
'''        
        