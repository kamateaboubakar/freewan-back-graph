import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        
# use it in your schema like following:
# from .sand_trips.types import SandTripsType, SandTripsFilter 
# from .sand_trips import queries as sand_trips_queries, mutations as sand_trips_mutations       
#    create_sand_trips = sand_trips_mutations.InsertSandTrips.Field()
#    update_sand_trips = sand_trips_mutations.UpdateSandTrips.Field()
#    sand_trips_queries.SandTripsQuery,


# 
# ********************* insertion class *********************
class InsertSandTrips(graphene.Mutation):
    success = graphene.Boolean()
    sand_trips = graphene.Field(types.SandTripsType)
    errors = graphene.String()

    class Arguments:

        amount = graphene.Float()
                    
        etd = graphene.Date()
                    
        eta = graphene.Date()
                    
        trip_details = graphene.JSONString(required=True)
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        > createSandTrips(amount:0.24186404845551335, etd:"2023-05-01", eta:"2023-09-24", tripDetails:""{"key":"value"}"", addedBy:)
        > {
>                success
>                errors
>                sandTrips   
        >             { 
>                                id 
>                                amount 
>                                etd 
>                                eta 
>                                tripDetails 
>                                isActive 
>                                isDeleted 
>                            addedBy 
>                                {
>                                    id
>                                } 
>                                createdDate 
>                                updatedDate
>       }
>    }
> }
''' 
        
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by'])
                    
            models.SandTrips.objects.create(**kwargs)
            return InsertSandTrips(sand_trips=models.SandTrips.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return InsertSandTrips(errors=error, success=False)
        


        
# ********************* update class *********************
class UpdateSandTrips(graphene.Mutation):
    success = graphene.Boolean()
    sand_trips = graphene.Field(types.SandTripsType)
    errors = graphene.String()

    class Arguments:

        id = graphene.ID(required=True)
                    
        amount = graphene.Float()
                    
        etd = graphene.Date()
                    
        eta = graphene.Date()
                    
        trip_details = graphene.JSONString()
                    
        is_active = graphene.Boolean()
                    
        is_deleted = graphene.Boolean()
                    
        added_by = graphene.ID(required=True)
                    
    class Meta:
        description = '''        
> mutation{
        
>    updateSandTrips(id:"", amount:0.1746065967259378, etd:"2023-11-23", eta:"2023-04-08", tripDetails:{"key":"value"}, isActive:false, isDeleted:true, addedBy:){
>                success
>                errors
>                sandTrips   
        >            { 
                            >    id 
                            >    amount 
                            >    etd 
                            >    eta 
                            >    tripDetails 
                            >    isActive 
                            >    isDeleted 
                            addedBy 
                                {
>                                    id
                                } 
                            >    createdDate 
                            >    updatedDate
>        }
>    }
> }''' 
        
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        
            kwargs['id'] = models.SandTrips.objects.get(id=kwargs['id']).id
                    
            kwargs['added_by'] = models.Users.objects.get(id=kwargs['added_by']).id
                    
            models.SandTrips.objects.filter(id=kwargs['id']).update(**kwargs)
            return UpdateSandTrips(sand_trips=models.SandTrips.objects.filter(**kwargs).all().latest('id'), success=True)
                    
        except Exception as error:
            return UpdateSandTrips(errors=error, success=False)
        