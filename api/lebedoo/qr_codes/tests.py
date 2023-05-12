#Mutation test request
        
                
'''        
mutation{
        > createQrCodes(code:"cuqdglqgzn", details:""{"key":"value"}"", addedBy:)
        
            {
                success
                errors
                qrCodes   
                        { 
                                id 
                                code 
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
        
>    updateQrCodes(id:"", code:"qpajynuops", details:{"key":"value"}, isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                qrCodes   
                        { 
                                id 
                                code 
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
        