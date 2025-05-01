from datetime import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")

session = db_session.create_session()

job = Jobs()
job.job = "deployment of residential modules 1 and 2"
job.team_leader_id = 1
job.work_size = 15
job.collaborators = "2, 3"
job.start_date = datetime.now()
job.is_finished = False

session.add(job)
session.commit()
