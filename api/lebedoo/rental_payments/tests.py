#Mutation test request
        
                
'''        
mutation{
        > createRentalPayments(amount:0.3185711111401426, paymentsDetails:""{"key":"value"}"", month:, year:, property:, propertyOwner:, propertyTenant:, addedBy:)
        
            {
                success
                errors
                rentalPayments   
                        { 
                                id 
                                amount 
                                paymentsDetails 
                            month 
                                {
                                    id
                                }
                             
                            year 
                                {
                                    id
                                }
                             
                            property 
                                {
                                    id
                                }
                             
                            propertyOwner 
                                {
                                    id
                                }
                             
                            propertyTenant 
                                {
                                    id
                                }
                             
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
        
>    updateRentalPayments(id:"", amount:0.5821984632747204, paymentsDetails:{"key":"value"}, month:, year:, property:, propertyOwner:, propertyTenant:, isActive:false, isDeleted:true, addedBy:)
            {
                success
                errors
                rentalPayments   
                        { 
                                id 
                                amount 
                                paymentsDetails 
                            month 
                                {
>                                    id
                                }
                             
                            year 
                                {
>                                    id
                                }
                             
                            property 
                                {
>                                    id
                                }
                             
                            propertyOwner 
                                {
>                                    id
                                }
                             
                            propertyTenant 
                                {
>                                    id
                                }
                             
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
        