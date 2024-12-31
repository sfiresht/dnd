from flask import Blueprint , request, jsonify
#from be.character import character


#name here is the name from the top of the folder so in our case: DnD.be.endpoints
#app = Flask(__name__)

races_bp = Blueprint("races", __name__)


@races_bp.route("/debug", methods=['GET'])
def debug():
    if request.method =='GET':
        return("this is a debug page for the races endpoint\n")
    # elif request.method == 'POST':
    #     data = request.get_json

@races_bp.route("/<name>", methods=['GET', 'POST'])
def race(name):
    if request.method =='GET':
        return("this is a debug page for the race endpoint {}\n".format(name))
        #here we should call the functions from the character code
        
