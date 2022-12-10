from dis import dis
from urllib import response
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with
from flask_restful import reqparse
from application.validation import BusinessValidationError, NotFoundError
from datetime import datetime
from flask import current_app as app
import werkzeug
from flask import jsonify, make_response
from application.model import classify_img
    

data_parser=reqparse.RequestParser()
data_parser.add_argument('image')

data_resource_fields = {
    'predicted_class':   fields.Integer,
    'image':    fields.String
}
class modelAPI(Resource):
    
    def get(self,image):
        image="./"+app.config['UPLOAD_FOLDER']+"/"+image
        response=dict()
        if image is None:
            raise BusinessValidationError(status_code=404, error_code="API_ERROR_01", error_message="File not found")
        else:
            print(image)
            print("Get predictions")
            output,img=classify_img(image)
            print(output)
            response['predicted_class']=output
            response = make_response(
                jsonify(
                    {"predicted_class": output,
                     "image":image}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response
