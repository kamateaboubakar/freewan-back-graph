#Mutation test request
        
                
'''        
mutation{
        > createPaymentMethods(name:"gclojtwxgm", abbreviated:"ozgjyauqra", addedBy:)
        
            {
                success
                errors
                paymentMethods   
                        { 
                                id 
                                name 
                                abbreviated 
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
        
>    updatePaymentMethods(id:"", name:"oravpauuqr", abbreviated:"ffzveewfts", isDeleted:true, addedBy:)
            {
                success
                errors
                paymentMethods   
                        { 
                                id 
                                name 
                                abbreviated 
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
        