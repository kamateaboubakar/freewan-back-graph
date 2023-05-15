import graphene
from .users import queries as users_queries, mutations as users_mutations
from .property import queries as property_queries, mutations as property_mutations
from .beverage_rack import queries as beverage_rack_queries, mutations as beverage_rack_mutations
from .beverage_rack_buyer import queries as beverage_rack_buyer_queries, mutations as beverage_rack_buyer_mutations
from .beverage_rack_owner import queries as beverage_rack_owner_queries, mutations as beverage_rack_owner_mutations
from .beverage_rack_payments import queries as beverage_rack_payments_queries, \
    mutations as beverage_rack_payments_mutations
from .property_owners import queries as property_owners_queries, mutations as property_owners_mutations
from .property_tenants import queries as property_tenants_queries, mutations as property_tenants_mutations
from .qr_codes import queries as qr_codes_queries, mutations as qr_codes_mutations
from .rental_payments import queries as rental_payments_queries, mutations as rental_payments_mutations
from .sand_buyer import queries as sand_buyer_queries, mutations as sand_buyer_mutations
from .sand_infos import queries as sand_infos_queries, mutations as sand_infos_mutations
from .sand_trip_payments import queries as sand_trip_payments_queries, mutations as sand_trip_payments_mutations
from .sand_trips import queries as sand_trips_queries, mutations as sand_trips_mutations
from .sand_vendors import queries as sand_vendors_queries, mutations as sand_vendors_mutations
from .company import queries as company_queries, mutations as company_mutations
from .address import queries as address_queries, mutations as address_mutations
from .cities import queries as cities_queries, mutations as cities_mutations
from .contacts import queries as contacts_queries, mutations as contacts_mutations
from .continent import queries as continent_queries, mutations as continent_mutations
from .country import queries as country_queries, mutations as country_mutations
from .currencies import queries as currencies_queries, mutations as currencies_mutations
from .department import queries as department_queries, mutations as department_mutations
from .gateways import queries as gateways_queries, mutations as gateways_mutations
from .job_function import queries as job_function_queries, mutations as job_function_mutations
from .job_profession import queries as job_profession_queries, mutations as job_profession_mutations
from .languages import queries as languages_queries, mutations as languages_mutations
from .months import queries as months_queries, mutations as months_mutations
from .municipalities import queries as municipalities_queries, mutations as municipalities_mutations
from .payment_methods import queries as payment_methods_queries, mutations as payment_methods_mutations
from .region import queries as region_queries, mutations as region_mutations
from .roles_privileges import queries as roles_privileges_queries, mutations as roles_privileges_mutations
from .status import queries as status_queries, mutations as status_mutations
from .transactions import queries as transactions_queries, mutations as transactions_mutations
from .user_privileges import queries as user_privileges_queries, mutations as user_privileges_mutations
from .user_roles import queries as user_roles_queries, mutations as user_roles_mutations
from .users_details import queries as users_details_queries, mutations as users_details_mutations
from .years import queries as years_queries, mutations as years_mutations
from .otp_codes import queries as otp_codes_queries, mutations as otp_codes_mutations


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
    company_queries.CompanyQuery,
    address_queries.AddressQuery,
    cities_queries.CitiesQuery,
    contacts_queries.ContactsQuery,
    continent_queries.ContinentQuery,
    country_queries.CountryQuery,
    currencies_queries.CurrenciesQuery,
    department_queries.DepartmentQuery,
    gateways_queries.GatewaysQuery,
    job_function_queries.JobFunctionQuery,
    job_profession_queries.JobProfessionQuery,
    languages_queries.LanguagesQuery,
    months_queries.MonthsQuery,
    municipalities_queries.MunicipalitiesQuery,
    payment_methods_queries.PaymentMethodsQuery,
    region_queries.RegionQuery,
    roles_privileges_queries.RolesPrivilegesQuery,
    status_queries.StatusQuery,
    transactions_queries.TransactionsQuery,
    user_privileges_queries.UserPrivilegesQuery,
    user_roles_queries.UserRolesQuery,
    users_details_queries.UsersDetailsQuery,
    years_queries.YearsQuery,
    otp_codes_queries.OtpCodesQuery,
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
    create_company = company_mutations.InsertCompany.Field()
    update_company = company_mutations.UpdateCompany.Field()
    create_address = address_mutations.InsertAddress.Field()
    update_address = address_mutations.UpdateAddress.Field()
    create_contacts = contacts_mutations.InsertContacts.Field()
    update_contacts = contacts_mutations.UpdateContacts.Field()
    create_continent = continent_mutations.InsertContinent.Field()
    update_continent = continent_mutations.UpdateContinent.Field()
    create_department = department_mutations.InsertDepartment.Field()
    update_department = department_mutations.UpdateDepartment.Field()
    create_currencies = currencies_mutations.InsertCurrencies.Field()
    update_currencies = currencies_mutations.UpdateCurrencies.Field()
    create_gateways = gateways_mutations.InsertGateways.Field()
    update_gateways = gateways_mutations.UpdateGateways.Field()
    create_job_function = job_function_mutations.InsertJobFunction.Field()
    update_job_function = job_function_mutations.UpdateJobFunction.Field()
    create_job_profession = job_profession_mutations.InsertJobProfession.Field()
    update_job_profession = job_profession_mutations.UpdateJobProfession.Field()
    create_languages = languages_mutations.InsertLanguages.Field()
    update_languages = languages_mutations.UpdateLanguages.Field()
    create_months = months_mutations.InsertMonths.Field()
    update_months = months_mutations.UpdateMonths.Field()
    create_municipalities = municipalities_mutations.InsertMunicipalities.Field()
    update_municipalities = municipalities_mutations.UpdateMunicipalities.Field()
    create_payment_methods = payment_methods_mutations.InsertPaymentMethods.Field()
    update_payment_methods = payment_methods_mutations.UpdatePaymentMethods.Field()
    create_region = region_mutations.InsertRegion.Field()
    update_region = region_mutations.UpdateRegion.Field()
    create_roles_privileges = roles_privileges_mutations.InsertRolesPrivileges.Field()
    update_roles_privileges = roles_privileges_mutations.UpdateRolesPrivileges.Field()
    create_status = status_mutations.InsertStatus.Field()
    update_status = status_mutations.UpdateStatus.Field()
    create_transactions = transactions_mutations.InsertTransactions.Field()
    update_transactions = transactions_mutations.UpdateTransactions.Field()
    create_user_privileges = user_privileges_mutations.InsertUserPrivileges.Field()
    update_user_privileges = user_privileges_mutations.UpdateUserPrivileges.Field()
    create_user_roles = user_roles_mutations.InsertUserRoles.Field()
    update_user_roles = user_roles_mutations.UpdateUserRoles.Field()
    create_user_roles = user_roles_mutations.InsertUserRoles.Field()
    update_user_roles = user_roles_mutations.UpdateUserRoles.Field()
    create_users_details = users_details_mutations.InsertUsersDetails.Field()
    update_users_details = users_details_mutations.UpdateUsersDetails.Field()
    create_years = years_mutations.InsertYears.Field()
    update_years = years_mutations.UpdateYears.Field()
    create_otp_codes = otp_codes_mutations.InsertOtpCodes.Field()
    update_otp_codes = otp_codes_mutations.UpdateOtpCodes.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
