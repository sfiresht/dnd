from flask import Blueprint, request, jsonify
#from be.character import character


#name here is the name from the top of the folder so in our case: DnD.be.endpoints
#app = Flask(__name__)

charcters_bp = Blueprint('charcters', __name__)



@charcters_bp.route("/debug", methods=['GET', 'POST'])
def debug():
    if request.method =='GET':
        return("this is a debug page for the races endpoint\n")
    elif request.method == 'POST':
        data = request.get_json

@charcters_bp.route("/<name>", methods=['GET', 'POST'])
def character(name):
    if request.method =='GET':
        return("this is a debug page for the charcter endpoint {}\n".format(name))
        #here we should call the functions from the character code
        pass

@charcters_bp.route("/create_char_page/<name>", methods=['POST'])
def create_char_page(name):
    pass

@charcters_bp.route("/create_char_page_random/", methods=['POST'])
def create_char_page_random(name):
    pass