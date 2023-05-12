DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

CREATE TABLE users
(
    id            VARCHAR(32) PRIMARY KEY,
    username      VARCHAR(32) UNIQUE,
    email         VARCHAR(255) UNIQUE NOT NULL,
    first_name    VARCHAR(255)        NOT NULL,
    last_name     VARCHAR(255)        NOT NULL,
    privileges    JSONB,
    is_admin      BOOLEAN,
    is_freelancer BOOLEAN,
    is_client     BOOLEAN,
    is_deleted    BOOLEAN                  DEFAULT FALSE,
    created_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE user_roles
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(32),
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE user_privileges
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(255),
    is_active  BOOLEAN DEFAULT true,
    is_deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE roles_privileges
(
    id           SERIAL PRIMARY KEY,
    privilege_id INT REFERENCES user_privileges (id),
    role_id      INT REFERENCES user_roles (id)
);

CREATE TABLE job_profession
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(255),
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE job_function
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(255),
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE company
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    legal_form   VARCHAR(50),
    logo         VARCHAR(255),
    address      JSONB,
    contact      JSONB,
    area         JSONB,
    added_by     VARCHAR REFERENCES users (id),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE continent
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE country
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    ext          INT,
    code         VARCHAR(3),
    continent_id INT REFERENCES continent (id),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()

);

CREATE TABLE region
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    country_id   INT REFERENCES country (id),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE department
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    region_id    INT REFERENCES region (id),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE cities
(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255),
    department_id INT REFERENCES department (id),
    is_active     BOOLEAN,
    is_deleted    BOOLEAN                  DEFAULT FALSE,
    created_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE municipalities
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    city_id      INT REFERENCES cities (id),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE contacts
(
    id           SERIAL PRIMARY KEY,
    users_id     VARCHAR REFERENCES users (id),
    country_id   INT REFERENCES country (id),
    phone_number VARCHAR(15),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE address
(
    id              SERIAL PRIMARY KEY,
    users_id        VARCHAR REFERENCES users (id),
    details         VARCHAR(255),
    municipality_id INT REFERENCES municipalities (id),
    department_id   INT REFERENCES department (id),
    region_id       INT REFERENCES region (id),
    city_id         INT REFERENCES cities (id),
    country_id      INT REFERENCES country (id),
    is_active       BOOLEAN,
    is_deleted      BOOLEAN                  DEFAULT FALSE,
    created_date    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date    TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE users_details
(
    id                SERIAL PRIMARY KEY,
    user_id           VARCHAR REFERENCES users (id),
    gender            VARCHAR(1),
    civil_title       VARCHAR(5),
    dob               DATE,
    image             VARCHAR(100),
    description       VARCHAR(255),
    company           INT REFERENCES company (id),
    job_profession_id INT REFERENCES job_profession (id),
    job_function_id   INT REFERENCES job_function (id),
    address           JSONB,
    contacts          JSONB,
    languages         JSONB,
    skills            JSONB,
    experiences       JSONB,
    links             JSONB,
    degrees           JSONB
);

CREATE TABLE languages
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(3),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE months
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE years
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


---------------- APPs tables

/* *************************************** PROPERTY RENTAL ******************************************/


CREATE TABLE property
(
    id           SERIAL PRIMARY KEY,
    code         VARCHAR(33),
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE property_owners
(
    id             SERIAL PRIMARY KEY,
    property_id    INT REFERENCES property (id),
    property_owner VARCHAR REFERENCES users (id),
    is_active      BOOLEAN DEFAULT false,
    is_deleted     BOOLEAN DEFAULT false
);

CREATE TABLE property_tenants
(
    id              SERIAL PRIMARY KEY,
    property_id     INT REFERENCES property (id),
    property_tenant VARCHAR REFERENCES users (id),
    is_active       BOOLEAN DEFAULT false,
    is_deleted      BOOLEAN DEFAULT false
);

CREATE TABLE rental_payments
(
    id               SERIAL PRIMARY KEY,
    amount           DOUBLE PRECISION,
    payments_details JSONB,
    month_id         INT REFERENCES months (id),
    year_id          INT REFERENCES years (id),
    property_id      INT REFERENCES property (id),
    property_owner   INT REFERENCES property_owners (id),
    property_tenant  INT REFERENCES property_tenants (id),
    is_active        BOOLEAN                  DEFAULT false,
    is_deleted       BOOLEAN                  DEFAULT false,
    added_by         VARCHAR REFERENCES users (id),
    created_date     TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date     TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

/* *************************************** SAND TRIPS ******************************************/

CREATE TABLE sand_infos
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255),
    details      JSONB,
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE sand_vendors
(
    id            SERIAL PRIMARY KEY,
    sand_infos_id INT REFERENCES sand_infos (id),
    sand_owner    VARCHAR REFERENCES users (id),
    is_active     BOOLEAN                  DEFAULT false,
    is_deleted    BOOLEAN                  DEFAULT false,
    created_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE sand_buyer
(
    id            SERIAL PRIMARY KEY,
    sand_infos_id INT REFERENCES sand_infos (id),
    sand_buyer    VARCHAR REFERENCES users (id),
    is_active     BOOLEAN                  DEFAULT false,
    is_deleted    BOOLEAN                  DEFAULT false,
    created_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE sand_trips
(
    id           SERIAL PRIMARY KEY,
    amount       DOUBLE PRECISION,
    etd          TIMESTAMP WITH TIME ZONE,
    eta          TIMESTAMP WITH TIME ZONE,
    trip_details JSONB,
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE sand_trip_payments
(
    id               SERIAL PRIMARY KEY,
    sand_trip        INT REFERENCES sand_trips (id),
    payments_infos   JSONB,
    sand_trip_owners INT REFERENCES sand_vendors (id),
    sand_trip_buyer  INT REFERENCES sand_buyer (id),
    is_active        BOOLEAN                  DEFAULT false,
    is_deleted       BOOLEAN                  DEFAULT false,
    added_by         VARCHAR REFERENCES users (id),
    created_date     TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date     TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

/* *************************************** BEVERAGE RACK ******************************************/

CREATE TABLE beverage_rack
(
    id           SERIAL PRIMARY KEY,
    amount       DOUBLE PRECISION,
    rack_details JSONB,
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE beverage_rack_owner
(
    id           SERIAL PRIMARY KEY,
    rack_id      INT REFERENCES beverage_rack (id),
    rack_owner   VARCHAR REFERENCES users (id),
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE beverage_rack_buyer
(
    id           SERIAL PRIMARY KEY,
    rack_id      INT REFERENCES beverage_rack (id),
    rack_buyer   VARCHAR REFERENCES users (id),
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


CREATE TABLE beverage_rack_payments
(
    id               SERIAL PRIMARY KEY,
    amount           DOUBLE PRECISION,
    payments_details JSONB,
    rack_id          INT REFERENCES beverage_rack (id),
    rack_owner       INT REFERENCES beverage_rack_owner (id),
    rack_buyer       INT REFERENCES beverage_rack_buyer (id),
    is_active        BOOLEAN                  DEFAULT false,
    is_deleted       BOOLEAN                  DEFAULT false,
    added_by         VARCHAR REFERENCES users (id),
    created_date     TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date     TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

/* *************************************** TONTINE ******************************************/

/* *************************************** QR CODES ******************************************/

CREATE TABLE qr_codes
(
    id           SERIAL PRIMARY KEY,
    code         varchar(255),
    details      JSONB,
    is_active    BOOLEAN                  DEFAULT false,
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

/* *************************************** PAYMENTS ******************************************/

CREATE TABLE payment_methods
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE status
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


CREATE TABLE currencies
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE gateways
(
    id           SERIAL PRIMARY KEY,
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE transactions
(
    id                UUID PRIMARY KEY,
    amount            DOUBLE PRECISION,
    description       VARCHAR(255),
    gateway_id        INT REFERENCES gateways (id), /* stripe, paypal, adyen */
    payment_method_id INT REFERENCES payment_methods (id), /* stripe, paypal, adyen */ /* card, ideal, paypal */
    currency_id       INT REFERENCES currencies (id), /* stripe, paypal, adyen */ /* card, ideal, paypal */
    status            INT REFERENCES status (id), /* pending, failed, captured, refunded */
    metadata          JSONB,
    added_by          VARCHAR REFERENCES users (id),
    is_active         BOOLEAN,
    is_deleted        BOOLEAN                  DEFAULT FALSE,
    created_date      TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date      TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);