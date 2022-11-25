from flask import Flask, request, render_template
from os import getenv

from flask_migrate import Migrate

from models import db
from views.books import books_app

app = Flask(__name__)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(books_app, url_prefix="/books")

with app.app_context():
    db.create_all()


app.config.update(
    ENV="development",
    SECRET_KEY="fhfsnbdfvahgfajhdfgbgbg",
)


@app.route("/", endpoint="index_page")
def main_page():
    print_request()
    return render_template("index.html")


def print_request():
    print("request:", request)
    print("request.method:", request.method)
    print("request.path:", request.path)





if __name__ == "__main__":
    app.run(debug=True)

