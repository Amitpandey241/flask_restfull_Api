from flask import Flask
from pymongo import MongoClient
from flask_restful import Api
from newProject.project1.flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] ='amqp://admin:admin@localhost:5672//'
celery = make_celery(app)
api = Api(app)
