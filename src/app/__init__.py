from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{config.DB_NAME}'
db = SQLAlchemy(app)
start_time = datetime.datetime.now().replace(microsecond=0)


from app import routes, models