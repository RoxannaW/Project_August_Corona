import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

app = Flask(__name__)

#S="B85918591859851"#example, still have to calculate the true value of S

@app.route("/")
def default():
    return "Hi, there :)"


@app.route('/get/Token', methods=['GET'])
def get_token():
    group_id_number = None
   
    if 'group_id' in request.args:
        group_id_number = str(request.args['group_id'])
    
    if group_id_number == "C99":
    #Maybe have to add in the form of a variable N?
        return "{'token': B85918591859851}" 
        #Maybe have  to add S in form of a variable?

    else:
         return "This is a message of error" + "<br>" + "<br>" + str(request.args)
        
    
@app.route('/get/Json', methods=['GET'])
def get():
    token_id_number = None
    if 'token_id' in request.args:
        token_id_number = str(request.args['token_id'])
    
    if token_id_number == "B85918591859851":
    #Maybe have to add in the form of a variable N?
        return jsonify(col_1=[3, 2, 1, 0], col_2=['a', 'b', 'c', 'd']) 
        #Have to add the information that is assigned to our group 

    else:
         return "This is a message of error" + "<br>" + "<br>" + str(request.args)


def main():
    
    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    

    settings_file = os.path.dirname(__file__) + "\\settings.json"
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)

    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()