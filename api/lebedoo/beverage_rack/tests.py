#Mutation test request
        
                
'''        
mutation{
        > createBeverageRack(amount:0.9667765521150018, rackDetails:""{"key":"value"}"")
        
            {
                success
                errors
                beverageRack   
                        { 
                                id 
                                amount 
                                rackDetails 
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
        
>    updateBeverageRack(id:"", amount:0.8686756283058468, rackDetails:{"key":"value"}, isActive:true, isDeleted:false)
            {
                success
                errors
                beverageRack   
                        { 
                                id 
                                amount 
                                rackDetails 
                                isActive 
                                isDeleted 
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        