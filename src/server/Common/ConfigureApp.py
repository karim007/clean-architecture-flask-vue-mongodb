from flask_jwt import JWT, jwt_required, current_identity
import Keys  as Keys
from Modules.UserModule.Application.AuthenticateUserQuery import AuthenticateUserQuery
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask import request
import shutil
import os



class ConfigureApp:

    def __init__(self):
        self.urlSPA="http://localhost:8080"

    def jwt(self, app):
        Keys.JWT_SECRET
        app.config['SECRET_KEY'] = Keys.JWT_SECRET
        authenticateUserQuery=AuthenticateUserQuery()
        return JWT(app, authenticateUserQuery.authenticate, authenticateUserQuery.identity)

    def swagger(self, app):
        filename, filename2 = self.get_files_names()
        shutil.copyfile(filename, filename2)

        swaggerui_blueprint = get_swaggerui_blueprint('/swagger','/static/swagger.json', 
            config={
                'app-name': 'flask template'
            })
        app.register_blueprint(swaggerui_blueprint,url_prefix= '/swagger')
    
    def cors(self, app):
        app.after_request(self.add_cors_headers)
        return  CORS(app, resources={r"*": {"origins": self.urlSPA}})
    
    def add_cors_headers(self, response):
        response.headers['Access-Control-Allow-Origin'] =self.urlSPA
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
              response.headers['Access-Control-Allow-Headers'] = headers
        return response
    
    def get_files_names(self): ## needed for because the npm run build remove it
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'swagger.json')
        filename2 = os.path.join(dirname, "..", 'static/swagger.json')
        return filename, filename2