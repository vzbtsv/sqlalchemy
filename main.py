from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")


session = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = "21"
user.position = "capitan"
user.speciality = "research engineer"
user.adreess = "module_1"
user.email = "scott_chief@mars.org"



user1 = User()
user1.surname = "Anaxagoros"
user1.name = "Oculus"
user1.position = "Aeon Scholar"
user1.speciality = "Pathstrider Phenomenology"
user1.address = "Simulated Universe, Sector 1"
user1.email = "anaxagoros@hcs.com"




user2 = User()
user2.surname = "Herta"
user2.position = "Master of the Herta Space Station"
user2.speciality = "Simulated Universe Development"
user2.address = "Herta Space Station, Core Sector"
user2.email = "herta@hcs.com"




user3 = User()
user3.surname = "Screwllum"
user3.age = 127
user3.position = "Mechanical Philosopher"
user3.speciality = "Quantum Robotics"
user3.address = "Planet Screwllum, Clockwork Mansion"
user3.email = "screwllum@clockwork.com"


session.add(user)
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()









