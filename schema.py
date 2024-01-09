from marshmallow import Schema, fields, post_load

class MallSchema(Schema):
    id = fields.Integer(dump_only=True) # dump_only means that this field is only for output
    name = fields.String(required=True)
    center_x = fields.Float(required=True)
    center_y = fields.Float(required=True)
    radius = fields.Float(required=False)

class CategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    category = fields.String(required=True)
    items = fields.String(required=False)

class ShelfNavigationSchema(Schema):
    id = fields.Integer(dump_only=True)
    mall_id = fields.Integer(required=True)
    start_x = fields.Float(required=True)
    start_y = fields.Float(required=True)
    end_x = fields.Float(required=True)
    end_y = fields.Float(required=True)
    shelf_distance = fields.Float(required=False)
    category_id = fields.Integer(required=True)
 

