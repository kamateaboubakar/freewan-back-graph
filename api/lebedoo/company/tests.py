#Mutation test request
        
                
'''        
mutation{
        > createCompany(name:"cddcgrxfaf", legalForm:"ehsqmntfmz", logo:"fxxeupvqpj", address:""{"key":"value"}"", contact:""{"key":"value"}"", area:""{"key":"value"}"", addedBy:)
        
            {
                success
                errors
                company   
                        { 
                                id 
                                name 
                                legalForm 
                                logo 
                                address 
                                contact 
                                area 
                            addedBy 
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
        
>    updateCompany(id:"", name:"svtdtrqlfi", legalForm:"przomchllp", logo:"kqmqgiuoml", address:{"key":"value"}, contact:{"key":"value"}, area:{"key":"value"}, addedBy:, isActive:false, isDeleted:false)
            {
                success
                errors
                company   
                        { 
                                id 
                                name 
                                legalForm 
                                logo 
                                address 
                                contact 
                                area 
                            addedBy 
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
        