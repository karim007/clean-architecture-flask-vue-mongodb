
from flask import Flask, jsonify, request, send_from_directory, render_template
from Common.ConfigureApp import ConfigureApp
from bson.json_util import dumps

from Modules.TechniquesModule.Application.TechniquesQueries import TechniquesQueries
from Modules.UserModule.Application.AuthenticateUserQuery import AuthenticateUserQuery

from flask_jwt import JWT, jwt_required, current_identity
import json

from flask import Response




app = Flask(__name__)
app.config.update(
    BUILDVERSION="0.0.1",
    # process={"env":"production"},
)
ConfigureApp().jwt(app)
ConfigureApp().swagger(app)
ConfigureApp().cors(app)

authenticateService = AuthenticateUserQuery()
techniquesService = TechniquesQueries()



@app.route('/')
def index():
    return render_template("index.html")



@app.route('/protected')
@jwt_required( )
def protected():
    name='%s' % current_identity
    print(name)
    return name

@app.route('/filter', methods=['GET'])
def get_data( ):
    value=request.args.get('name')
    data =dumps( techniquesService.Filter(value))
    return Response(data, mimetype='application/json')
 

@app.route('/Post', methods=['Post'])
def post_data( ):
    tech=request.get_json()
    return dumps( techniquesService.Post(tech))



@app.route('/static/<path:path>')
def send_static(file):
    return send_from_directory('static/',file)

##Theses routes are needed because the npm build automation.
## If you copy past the build folder, change the url and remoce theses routes

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/manifest.json')
def send_manifest(path):
    return send_from_directory('static', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)


if __name__ == '__main__':
    app.run(port=5003)



