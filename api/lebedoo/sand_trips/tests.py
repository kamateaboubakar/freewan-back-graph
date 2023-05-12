#Mutation test request
        
                
'''        
mutation{
        > createSandTrips(amount:0.24186404845551335, etd:"2023-05-01", eta:"2023-09-24", tripDetails:""{"key":"value"}"", addedBy:)
        
            {
                success
                errors
                sandTrips   
                        { 
                                id 
                                amount 
                                etd 
                                eta 
                                tripDetails 
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
        
>    updateSandTrips(id:"", amount:0.1746065967259378, etd:"2023-11-23", eta:"2023-04-08", tripDetails:{"key":"value"}, isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                sandTrips   
                        { 
                                id 
                                amount 
                                etd 
                                eta 
                                tripDetails 
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
        