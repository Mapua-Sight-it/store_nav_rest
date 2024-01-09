from db import db 

class CategoryModel(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    items = db.Column(db.String(80), nullable=True)

    shelf_navigations = db.relationship('ShelfNavigationModel',back_populates='categories')
