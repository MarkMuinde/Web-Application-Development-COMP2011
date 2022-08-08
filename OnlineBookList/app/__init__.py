import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

app=Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
from app import views, models
