CREATE DATABASE IF NOT EXISTS marketplace_db;

CREATE TABLE IF NOT EXISTS customer
(
    customer_id serial NOT NULL PRIMARY KEY,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(50) NOT NULL UNIQUE,
    phone_number character varying(20) NOT NULL,
    password character varying(50) NOT NULL,
    salt character varying(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS shop
(
    shop_id serial NOT NULL PRIMARY KEY,
    name character varying(70) NOT NULL UNIQUE,
    description text,
    email character varying(50) NOT NULL,
    phone_number character varying(50) NOT NULL
    category_id serial NOT NULL
);

CREATE TABLE IF NOT EXISTS shop_category
(
    shop_category_id serial NOT NULL PRIMARY KEY,
    name character varying(50) NOT NULL UNIQUE,
    description text
);

CREATE TABLE IF NOT EXISTS product
(
    product_id serial NOT NULL  PRIMARY KEY,
    name character varying(80) NOT NULL,
    description text,
    price numeric NOT NULL,
    quantity integer NOT NULL,
    shop_id serial NOT NULL
);
