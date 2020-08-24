from flask import Flask , jsonify , request , abort
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

    # # this method return a josinfy object with a key of msg. and value  of hello world \
    #     -----------------------------------------------------------------------------
    @app.after_request
    def after_request(response):
        response.headers.add('Acess-Control-Allow-Headers' , 'Content-type' , 'Authorization')
        response.headers.add('Acess-Control-Allow-Methods' , 'GET,POST,PATCH,DELETE,OPTIONS')
        return response
    @app.route('/plants')
    def get_plants():
        page = request.args.get('page',1,type=int)
        #on the request object look at the arguments object and get the value of key 'page'
        #if that key does not exist return 1 ( default) and specify the type of that it is integer
        '''
        In flask, when a request is received 
        with query params the route in the @app.route decorator
         remains the same and the request object arguments contains the parameter. You access
          it as shown below. request.args is a Python dictionary so we use the get method 
        to access the value and provide a default value, in this case 1. 
        '''
        start=(page-1)*10
        end=start+10
        #what plants iam gonna start with
        plants = Plant.query.all()
        formatted_plants =[plant.format() for plant in plants] 
        return jsonify ({
            'sucess':True,
            'plants':formatted_plants[start:end],
            'total-plants' : len(formatted_plants)
        })
        
    @app.route('/plants/<int:plant_id>') #specify the plant id at the localhost link and rerturn 1 item eli bel id da
    
    def get_specific_plant(plant_id):
        plant=Plant.query.filter(Plant.id==plant_id).one_or_none()
        
        if plant is None
        abort(404)
        
        else:
            return jsonify({
                'sucess':True
                'plant':plant.format()
            })
    return app 
#  after creating the app , it must be returned to the user in order to allow uasge it .
# /////////////////////////////////////////////////////////////////
# if test_config is None
#  means if we are not in testing mode 