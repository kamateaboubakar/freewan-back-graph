#Mutation test request
        
                
'''        
mutation{
        > createAddress(users:, details:"xqwhhwlpqj", municipality:, department:, region:, city:, country:)
        
            {
                success
                errors
                address   
                        { 
                                id 
                            users 
                                {
                                    id
                                }
                             
                                details 
                            municipality 
                                {
                                    id
                                }
                             
                            department 
                                {
                                    id
                                }
                             
                            region 
                                {
                                    id
                                }
                             
                            city 
                                {
                                    id
                                }
                             
                            country 
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
        
>    updateAddress(id:"", users:, details:"maxwwtpowj", municipality:, department:, region:, city:, country:, isActive:false, isDeleted:true)
            {
                success
                errors
                address   
                        { 
                                id 
                            users 
                                {
>                                    id
                                }
                             
                                details 
                            municipality 
                                {
>                                    id
                                }
                             
                            department 
                                {
>                                    id
                                }
                             
                            region 
                                {
>                                    id
                                }
                             
                            city 
                                {
>                                    id
                                }
                             
                            country 
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
        