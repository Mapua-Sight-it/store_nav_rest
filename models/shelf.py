from db import db

class ShelfNavigationModel(db.Model):
    __tablename__ = 'shelf_navigations'

    id = db.Column(db.Integer, primary_key=True)
    mall_id = db.Column(db.Integer, db.ForeignKey('malls.id'))
    start_x = db.Column(db.Float(precision=16), nullable=False)
    start_y = db.Column(db.Float(precision=16), nullable=False)
    end_x = db.Column(db.Float(precision=16), nullable=False)
    end_y = db.Column(db.Float(precision=16), nullable=False)
    shelf_distance = db.Column(db.Float(precision=16), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    malls = db.relationship('MallModel',back_populates='shelf_navigations')
    categories = db.relationship('CategoryModel',back_populates='shelf_navigations')
