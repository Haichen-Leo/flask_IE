from db_util import db

Base = db.Model


class Feedback(Base):
    __tablename__ = "feedback"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))


if __name__ == '__main__':
    from db_util import create_app

    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()