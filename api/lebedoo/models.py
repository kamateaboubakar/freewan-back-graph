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


class Rents(models.Model):
    amount = models.CharField(max_length=32, blank=True, null=True)
    month = models.ForeignKey(Months, models.DO_NOTHING, blank=True, null=True)
    year = models.ForeignKey('Years', models.DO_NOTHING, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rents'


class RolesPrivileges(models.Model):
    privilege = models.ForeignKey('UserPrivileges', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('UserRoles', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_privileges'


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
    amount = models.IntegerField(blank=True, null=True)
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
    email = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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
