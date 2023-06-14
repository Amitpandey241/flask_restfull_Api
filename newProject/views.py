from newProject import app
from project1.views import example
# from newProject.project1.flask_celery import  make_celery

app.register_blueprint(example)

if __name__ == "__main__":
    app.run(debug=True)
