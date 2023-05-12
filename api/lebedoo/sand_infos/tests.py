#Mutation test request
        
                
'''        
mutation{
        > createSandInfos(name:"xlozdagghw", details:""{"key":"value"}"", addedBy:)
        
            {
                success
                errors
                sandInfos   
                        { 
                                id 
                                name 
                                details 
                                isActive 
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
        
>    updateSandInfos(id:"", name:"mjnaokbmne", details:{"key":"value"}, isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                sandInfos   
                        { 
                                id 
                                name 
                                details 
                                isActive 
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
        