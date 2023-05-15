# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.ForeignKey('Municipalities', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('Cities', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class BeverageRack(models.Model):
    amount = models.FloatField(blank=True, null=True)
    rack_details = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beverage_rack'


class BeverageRackBuyer(models.Model):
    rack = models.ForeignKey(BeverageRack, models.DO_NOTHING, blank=True, null=True)
    rack_buyer = models.ForeignKey('Users', models.DO_NOTHING, db_column='rack_buyer', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beverage_rack_buyer'


class BeverageRackOwner(models.Model):
    rack = models.ForeignKey(BeverageRack, models.DO_NOTHING, blank=True, null=True)
    rack_owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='rack_owner', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beverage_rack_owner'


class BeverageRackPayments(models.Model):
    amount = models.FloatField(blank=True, null=True)
    payments_details = models.JSONField(blank=True, null=True)
    rack = models.ForeignKey(BeverageRack, models.DO_NOTHING, blank=True, null=True)
    rack_owner = models.ForeignKey(BeverageRackOwner, models.DO_NOTHING, db_column='rack_owner', blank=True, null=True)
    rack_buyer = models.ForeignKey(BeverageRackBuyer, models.DO_NOTHING, db_column='rack_buyer', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beverage_rack_payments'


class Cities(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class Company(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    legal_form = models.CharField(max_length=50, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    contact = models.JSONField(blank=True, null=True)
    area = models.JSONField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Contacts(models.Model):
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class Continent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'continent'


class Country(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ext = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    continent = models.ForeignKey(Continent, models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Currencies(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    abbreviated = models.CharField(max_length=2, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Gateways(models.Model):
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateways'


class JobFunction(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_function'


class JobProfession(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_profession'


class Languages(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    abbreviated = models.CharField(max_length=3, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Months(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    abbreviated = models.CharField(max_length=2, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'months'


class Municipalities(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(Cities, models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipalities'


class OtpCodes(models.Model):
    otp_code = models.CharField(max_length=4, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=32, blank=True, null=True)
    country_code = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_code', blank=True, null=True)
    expiry_time = models.IntegerField(blank=True, null=True)
    is_expired = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_codes'


class PaymentMethods(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    abbreviated = models.CharField(max_length=2, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_methods'


class Property(models.Model):
    code = models.CharField(max_length=33, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class PropertyOwners(models.Model):
    property = models.ForeignKey(Property, models.DO_NOTHING, blank=True, null=True)
    property_owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='property_owner', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property_owners'


class PropertyTenants(models.Model):
    property = models.ForeignKey(Property, models.DO_NOTHING, blank=True, null=True)
    property_tenant = models.ForeignKey('Users', models.DO_NOTHING, db_column='property_tenant', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property_tenants'


class QrCodes(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    details = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qr_codes'


class Region(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class RentalPayments(models.Model):
    amount = models.FloatField(blank=True, null=True)
    payments_details = models.JSONField(blank=True, null=True)
    month = models.ForeignKey(Months, models.DO_NOTHING, blank=True, null=True)
    year = models.ForeignKey('Years', models.DO_NOTHING, blank=True, null=True)
    property = models.ForeignKey(Property, models.DO_NOTHING, blank=True, null=True)
    property_owner = models.ForeignKey(PropertyOwners, models.DO_NOTHING, db_column='property_owner', blank=True, null=True)
    property_tenant = models.ForeignKey(PropertyTenants, models.DO_NOTHING, db_column='property_tenant', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental_payments'


class RolesPrivileges(models.Model):
    privilege = models.ForeignKey('UserPrivileges', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('UserRoles', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_privileges'


class SandBuyer(models.Model):
    sand_infos = models.ForeignKey('SandInfos', models.DO_NOTHING, blank=True, null=True)
    sand_buyer = models.ForeignKey('Users', models.DO_NOTHING, db_column='sand_buyer', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sand_buyer'


class SandInfos(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    details = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sand_infos'


class SandTripPayments(models.Model):
    sand_trip = models.ForeignKey('SandTrips', models.DO_NOTHING, db_column='sand_trip', blank=True, null=True)
    payments_infos = models.JSONField(blank=True, null=True)
    sand_trip_owners = models.ForeignKey('SandVendors', models.DO_NOTHING, db_column='sand_trip_owners', blank=True, null=True)
    sand_trip_buyer = models.ForeignKey(SandBuyer, models.DO_NOTHING, db_column='sand_trip_buyer', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sand_trip_payments'


class SandTrips(models.Model):
    amount = models.FloatField(blank=True, null=True)
    etd = models.DateTimeField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    trip_details = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sand_trips'


class SandVendors(models.Model):
    sand_infos = models.ForeignKey(SandInfos, models.DO_NOTHING, blank=True, null=True)
    sand_owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='sand_owner', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sand_vendors'


class SecurityQuestions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_questions'


class Status(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    abbreviated = models.CharField(max_length=2, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    gateway = models.ForeignKey(Gateways, models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethods, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(Currencies, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING, db_column='status', blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserPrivileges(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_privileges'


class UserRoles(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(unique=True, max_length=32, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=32, blank=True, null=True)
    country_code = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_code', blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    privileges = models.JSONField(blank=True, null=True)
    is_admin = models.BooleanField(blank=True, null=True)
    is_freelancer = models.BooleanField(blank=True, null=True)
    is_client = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersDetails(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    civil_title = models.CharField(max_length=5, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='company', blank=True, null=True)
    job_profession = models.ForeignKey(JobProfession, models.DO_NOTHING, blank=True, null=True)
    job_function = models.ForeignKey(JobFunction, models.DO_NOTHING, blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    contacts = models.JSONField(blank=True, null=True)
    languages = models.JSONField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    experiences = models.JSONField(blank=True, null=True)
    links = models.JSONField(blank=True, null=True)
    degrees = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_details'


class UsersSecurityQuestions(models.Model):
    questions = models.ForeignKey(SecurityQuestions, models.DO_NOTHING, blank=True, null=True)
    question_answers = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_security_questions'


class Years(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    abbreviated = models.CharField(max_length=2, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'years'
