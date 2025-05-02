from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os

#from src.entities.customer import Customer
#from src.registration_login.create_customer import create_customer
#from src.registration_login.password import generate_password_hash
#from src.registration_login.check_login import check_login
#from src.database_connection import cursor, conn
from src.registration_login.landing import process_landing
app = Flask(__name__)

load_dotenv()
# app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return process_landing(request.form)
    return render_template("landing.html")