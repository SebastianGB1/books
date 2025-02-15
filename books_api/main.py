import connexion
from db import db
from ma import ma


conex_app = connexion.App(__name__, specification_dir="./")
conex_app.add_api("booksAPI.yml")


app = conex_app.app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
ma.init_app(app)

# Initialize database tables
with app.app_context():
    db.create_all()

print("📌 Rutas registradas en Flask:")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
