from models import db, Gender
from app import app

with app.app_context():
    male=Gender("Male")
    female=Gender("Female")