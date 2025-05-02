from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os

from src.registration_login.landing import process_landing
app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return process_landing(request.form)
    return render_template("landing.html")