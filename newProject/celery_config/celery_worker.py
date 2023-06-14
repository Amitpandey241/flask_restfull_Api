# from celery import Celery
#
# def make_celery(app):
#     celery_app= Celery(
#         app,
#         backend= app.config['CELERY_RESULT_BACKEND'],
#         broker=app.config['CELERY_BROKER_URL'],
#         include=['newProject', 'newProject.celery_config.celery_task']
#     )
#     celery_app.conf.update(app.config)
#     class ContextTask(celery_app.Task):
#         def __call__(self, *args, **kwargs):
#
#
