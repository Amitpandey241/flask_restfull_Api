from flask import Flask
from pymongo import MongoClient
from flask_restful import Api
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required
import secrets
from celery import Celery


# def make_celery(app):
#     celery = Celery(app.import_name,broker='amqp://admin:admin@localhost:5672/',include=['newProject.project1.views'])
#     celery.conf.update(app.config)
#     TaskBase = celery.Task
#     class ContextTask(TaskBase):
#         abstract = True
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self,*args,**kwargs)
#     celery.Task = ContextTask
#     return celery

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secrets.token_hex(16)

jwt = JWTManager(app)
print("fdsf")
# app.config['CELERY_BROKER_URL'] ='amqp://admin:admin@localhost:5672//'

# celery = make_celery(app)
api = Api(app)
