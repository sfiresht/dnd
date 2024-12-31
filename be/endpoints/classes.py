from flask import Blueprint , request, jsonify
#from be.character import character


#name here is the name from the top of the folder so in our case: DnD.be.endpoints
#app = Flask(__name__)

classes_bp = Blueprint('classes', __name__)




@classes_bp.route("/debug", methods=['GET', 'POST'])
def debug():
    if request.method =='GET':
        return("this is a debug page for the classes endpoint\n")
    elif request.method == 'POST':
        data = request.get_json

@classes_bp.route("/<name>", methods=['GET', 'POST'])
def classes(name):
    if request.method =='GET':
        return("this is a debug page for the class endpoint {}\n".format(name))
        
        #here we should call the functions from the character code
        

