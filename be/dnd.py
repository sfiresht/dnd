import psycopg2
#from configuration.config import *
from flask import Flask
from endpoints.races import races_bp
from endpoints.classes import classes_bp
from endpoints.charcters import charcters_bp


#### load configuration section #####


#### API section #####
#name here is the name from the top of the folder so in our case: DnD.be.endpoints
app = Flask(__name__, instance_relative_config=True)
print("starting endpoints app")
print("app name is {}".format(app.name))

#load configuration from object
app.config.from_object('configuration.config.default')
# registering the blusprints
app.register_blueprint(races_bp, url_prefix='/races')
app.register_blueprint(classes_bp, url_prefix='/classes')
app.register_blueprint(charcters_bp, url_prefix='/charcters')
#individual endpoint for debug
@app.route("/debug")
def sanity_check():
    return "OK :)\n"


#### DB section #####

#db = psycopg2.connect(host=app.config['DB_ADDRESS'], port=app.config['DB_PORT'] ,dbname=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASSWORD'])
#cur = db.cursor()

#print(cur.execute("select * from public.classes"))

# records = cur.fetchall()
# print(records)


# def get_query():
#     print('inside get query')
#     cur.execute("select * from public.classes")
#     records = cur.fetchall()
#     return records

# def insert_query():
#     cur.execute("insert to public.classes () values ()")
#     records = cur.fetchall()
#     return records



#print(get_query())


if __name__ == "__main__": 
    print('url map:')
    print(app.url_map)
    #print(get_query())
    app.run(host=app.config['APP_ADDRESS'], port=app.config['APP_PORT'], debug=True)
    
    

