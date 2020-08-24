from flask import Flask , jsonify
from models import setup_db , Plant
from flask_cors import CORS 
def create_app(test_config=None):
    #Create and config the app
    # 
    # Once Flask-CORS is installed, you simply import the CORS function and call it with your 
    # app instance as a parameter. This will intialize Flask-CORS will all default options. 
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    # app routing methoed define route that we are heading to it 
    @app.route("/hello")
    # @cross_origin()
    def get_greeting():
        return jsonify({'message':'Hello, World!'})
    # # this method return a josinfy object with a key of msg. and value  of hello world \
    #     -----------------------------------------------------------------------------
    @app.after_request
    def after_request(response):
        response.headers.add('Acess-Control-Allow-Headers' , 'Content-type' , 'Authorization')
        response.headers.add('Acess-Control-Allow-Methods' , 'GET,POST,PATCH,DELETE,OPTIONS')
        return response
    @app.route('/simely') 
    def simely():
        return  ':)'
                        
    return app 
#  after creating the app , it must be returned to the user in order to allow uasge it .
# /////////////////////////////////////////////////////////////////
# if test_config is None
#  means if we are not in testing mode 