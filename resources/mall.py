from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models import MallModel, ShelfNavigationModel, CategoryModel

from schema import MallSchema

from db import db

blp = Blueprint("Mall",__name__, description="Mall operations")

@blp.route("/malls")
class Malls(MethodView):

    @blp.response(200, MallSchema(many=True))
    def get(self):
        """Get all malls"""
        malls = MallModel.query.all()
        return malls
    
    def delete(self):
        """Delete all malls"""
        try:
            MallModel.query.delete()
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"Internal server error: {e}")

        return {"message": "All malls deleted"}

@blp.route("/mall")
class Mall(MethodView):

    @blp.arguments(MallSchema)
    @blp.response(201, MallSchema)
    def post(self,mall_data):
        
        #Create new mall
        mall = MallModel(**mall_data)
        try:
            db.session.add(mall)
            db.session.commit()
        except IntegrityError:
            abort(409, message="Mall already exists")
        except SQLAlchemyError as e:
            abort(500, message=f"Internal server error: {e}")

        return mall