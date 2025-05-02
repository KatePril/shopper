from flask import render_template, session
from src.registration_login.check_login import check_login
from src.database_connection import cursor, conn
from src.entities.customer import Customer
from src.registration_login.create_customer import create_customer
from src.registration_login.password import generate_password_hash

def process_landing(form):
    form_type = form.get("form_type")
    if form_type == "sign_in":
        customer_id = check_login(
            email=form.get("login_email"),
            password=form.get("login_password"),
            cursor=cursor,
        )
        if customer_id is None:
            message = "Email or password is incorrect"
            return render_template("landing.html", message=message)
    elif form_type == "sign_up":
        customer = Customer(
            first_name=form.get("register_first_name"),
            last_name=form.get("register_last_name"),
            email=form.get("register_email"),
            phone_number=form.get("register_phone_number"),
            password=form.get("register_password")
        )
        customer.password = generate_password_hash(customer.password)
        customer_id = create_customer(customer, cursor, conn)
        session["customer_id"] = customer_id