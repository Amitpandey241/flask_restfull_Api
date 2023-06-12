from newProject import app
from newProject.project1.views import example
app.register_blueprint(example)

if __name__ == "__main__":
    app.run(debug=True)
