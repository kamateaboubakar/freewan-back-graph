#Mutation test request
        
                
'''        
mutation{
        > createContinent(name:"elqomkdzab",)
        
            {
                success
                errors
                continent   
                        { 
                                id 
                                name 
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
        
>    updateContinent(id:"", name:"qhmxdyxqkl", isActive:false, isDeleted:true)
            {
                success
                errors
                continent   
                        { 
                                id 
                                name 
                                isActive 
                                isDeleted 
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        