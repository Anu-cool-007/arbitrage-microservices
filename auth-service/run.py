from app import create_app, db
from app import models
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()
    # Check if the existing table contain data, if not then initialize the table
    s = db.session()
    if len(s.query(models.User).all()) == 0:
        engine = s.get_bind()
        db.metadata.create_all(engine)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
