import graphene
from .users import queries as users_queries, mutations as users_mutations
from .property import queries as property_queries, mutations as property_mutations
from .beverage_rack import queries as beverage_rack_queries, mutations as beverage_rack_mutations
from .beverage_rack_buyer import queries as beverage_rack_buyer_queries, mutations as beverage_rack_buyer_mutations
from .beverage_rack_owner import queries as beverage_rack_owner_queries, mutations as beverage_rack_owner_mutations
from .beverage_rack_payments import queries as beverage_rack_payments_queries, mutations as beverage_rack_payments_mutations
from .property_owners import queries as property_owners_queries, mutations as property_owners_mutations
from .property_tenants import queries as property_tenants_queries, mutations as property_tenants_mutations
from .qr_codes import queries as qr_codes_queries, mutations as qr_codes_mutations
from .rental_payments import queries as rental_payments_queries, mutations as rental_payments_mutations
from .sand_buyer import queries as sand_buyer_queries, mutations as sand_buyer_mutations
from .sand_infos import queries as sand_infos_queries, mutations as sand_infos_mutations
from .sand_trip_payments import queries as sand_trip_payments_queries, mutations as sand_trip_payments_mutations
from .sand_trips import queries as sand_trips_queries, mutations as sand_trips_mutations
from .sand_vendors import queries as sand_vendors_queries, mutations as sand_vendors_mutations







class Query(
    users_queries.UsersQuery,
    property_queries.PropertyQuery,
    beverage_rack_queries.BeverageRackQuery,
    beverage_rack_buyer_queries.BeverageRackBuyerQuery,
    beverage_rack_owner_queries.BeverageRackOwnerQuery,
    beverage_rack_payments_queries.BeverageRackPaymentsQuery,
    property_owners_queries.PropertyOwnersQuery,
    property_tenants_queries.PropertyTenantsQuery,
    qr_codes_queries.QrCodesQuery,
    rental_payments_queries.RentalPaymentsQuery,
    sand_buyer_queries.SandBuyerQuery,
    sand_infos_queries.SandInfosQuery,
    sand_trip_payments_queries.SandTripPaymentsQuery,
    sand_trips_queries.SandTripsQuery,
    sand_vendors_queries.SandVendorsQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_users = users_mutations.InsertUsers.Field()
    update_users = users_mutations.UpdateUsers.Field()
    create_property = property_mutations.InsertProperty.Field()
    update_property = property_mutations.UpdateProperty.Field()
    create_beverage_rack = beverage_rack_mutations.InsertBeverageRack.Field()
    update_beverage_rack = beverage_rack_mutations.UpdateBeverageRack.Field()
    create_beverage_rack_buyer = beverage_rack_buyer_mutations.InsertBeverageRackBuyer.Field()
    update_beverage_rack_buyer = beverage_rack_buyer_mutations.UpdateBeverageRackBuyer.Field()
    create_beverage_rack_owner = beverage_rack_owner_mutations.InsertBeverageRackOwner.Field()
    update_beverage_rack_owner = beverage_rack_owner_mutations.UpdateBeverageRackOwner.Field()
    create_beverage_rack_payments = beverage_rack_payments_mutations.InsertBeverageRackPayments.Field()
    update_beverage_rack_payments = beverage_rack_payments_mutations.UpdateBeverageRackPayments.Field()
    create_property_owners = property_owners_mutations.InsertPropertyOwners.Field()
    update_property_owners = property_owners_mutations.UpdatePropertyOwners.Field()
    create_property_tenants = property_tenants_mutations.InsertPropertyTenants.Field()
    update_property_tenants = property_tenants_mutations.UpdatePropertyTenants.Field()
    create_qr_codes = qr_codes_mutations.InsertQrCodes.Field()
    update_qr_codes = qr_codes_mutations.UpdateQrCodes.Field()
    create_rental_payments = rental_payments_mutations.InsertRentalPayments.Field()
    update_rental_payments = rental_payments_mutations.UpdateRentalPayments.Field()
    create_sand_buyer = sand_buyer_mutations.InsertSandBuyer.Field()
    update_sand_buyer = sand_buyer_mutations.UpdateSandBuyer.Field()
    create_sand_infos = sand_infos_mutations.InsertSandInfos.Field()
    update_sand_infos = sand_infos_mutations.UpdateSandInfos.Field()
    create_sand_trip_payments = sand_trip_payments_mutations.InsertSandTripPayments.Field()
    update_sand_trip_payments = sand_trip_payments_mutations.UpdateSandTripPayments.Field()
    create_sand_trips = sand_trips_mutations.InsertSandTrips.Field()
    update_sand_trips = sand_trips_mutations.UpdateSandTrips.Field()
    create_sand_vendors = sand_vendors_mutations.InsertSandVendors.Field()
    update_sand_vendors = sand_vendors_mutations.UpdateSandVendors.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
