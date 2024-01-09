from db import db 

class MallModel(db.Model):

    __tablename__ = 'malls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    center_x = db.Column(db.Float(precision=16), nullable=False)
    center_y = db.Column(db.Float(precision=16), nullable=False)
    radius = db.Column(db.Float(precision=16), nullable=False)

    shelf_navigations = db.relationship('ShelfNavigationModel',back_populates='malls')

    