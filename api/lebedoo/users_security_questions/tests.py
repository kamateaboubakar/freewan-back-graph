#Mutation test request
        
                
'''        
mutation{
        > createUsersSecurityQuestions(questions:, questionAnswers:"pbhdgtvold", user:)
        
            {
                success
                errors
                usersSecurityQuestions   
                        { 
                                id 
                            questions 
                                {
                                    id
                                }
                             
                                questionAnswers 
                            user 
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
        
>    updateUsersSecurityQuestions(id:"", questions:, questionAnswers:"payusivkxe", user:)
            {
                success
                errors
                usersSecurityQuestions   
                        { 
                                id 
                            questions 
                                {
>                                    id
                                }
                             
                                questionAnswers 
                            user 
                                {
>                                    id
                                }
                             
                                createdDate 
                                updatedDate
        }
    }
}
        
'''        
        