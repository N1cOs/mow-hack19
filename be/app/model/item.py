from app.app import db

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.String(511), nullable=False)

    