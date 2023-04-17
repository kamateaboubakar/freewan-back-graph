DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

CREATE TABLE users
(
    id              VARCHAR(32)  PRIMARY KEY,
    username        VARCHAR(32)  UNIQUE,
    email           VARCHAR(255) UNIQUE NOT NULL,
    first_name      VARCHAR(255)        NOT NULL,
    last_name       VARCHAR(255)        NOT NULL,
    privileges      JSONB,
    is_admin        BOOLEAN,
    is_freelancer   BOOLEAN,
    is_client       BOOLEAN,
    is_deleted      BOOLEAN                  DEFAULT FALSE,
    created_date    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date    TIMESTAMP WITH TIME ZONE DEFAULT NOW()
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
    id        SERIAL PRIMARY KEY,
    privilege_id INT REFERENCES user_privileges (id),
    role_id     INT REFERENCES user_roles (id)
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
    id   SERIAL PRIMARY KEY,
    name VARCHAR(255),
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
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(255),
    country_id INT REFERENCES country (id),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE department
(
    id        SERIAL PRIMARY KEY,
    name      VARCHAR(255),
    region_id INT REFERENCES region (id),
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
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE municipalities
(
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(255),
    city_id INT REFERENCES cities (id),
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
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE users_details
(
    id                SERIAL PRIMARY KEY,
    user_id           VARCHAR REFERENCES users (id),
    gender            VARCHAR(1),
    civil_title       VARCHAR(5),
    dob               DATE,
    image             VARCHAR(100),
    description       VARCHAR(255) ,
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

CREATE TABLE languages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32),
    abbreviated VARCHAR(3),
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


---------------- APPs tables


CREATE TABLE months (
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE years (
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(32),
    abbreviated  VARCHAR(2),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


CREATE TABLE rents
(
    id           SERIAL PRIMARY KEY,
    amount       VARCHAR(32),
    month_id     INT REFERENCES months (id),
    year_id      INT REFERENCES years (id),
    is_deleted   BOOLEAN                  DEFAULT false,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


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

CREATE TABLE gateways (
    id SERIAL PRIMARY KEY,
    is_active    BOOLEAN,
    is_deleted   BOOLEAN                  DEFAULT FALSE,
    added_by     VARCHAR REFERENCES users (id),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE transactions (
  id                   UUID PRIMARY KEY,
  amount               INT,
  description          VARCHAR(255),
  gateway_id           INT REFERENCES gateways (id),  /* stripe, paypal, adyen */
  payment_method_id    INT REFERENCES payment_methods (id),  /* stripe, paypal, adyen */ /* card, ideal, paypal */
  currency_id          INT REFERENCES currencies (id),  /* stripe, paypal, adyen */ /* card, ideal, paypal */
  status               INT REFERENCES status (id),  /* pending, failed, captured, refunded */
  metadata             JSONB,
  added_by             VARCHAR REFERENCES users (id),
  is_active            BOOLEAN,
  is_deleted           BOOLEAN                  DEFAULT FALSE,
  created_date         TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_date         TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);