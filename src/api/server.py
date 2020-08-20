import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

app = Flask(__name__)



@app.route("/")
def default():
    return "Hi, there :)"


@app.route('/get/Token', methods=['GET'])
def get_token():
    group_id_number = None
    N = "C99"
   
    if 'group_id' in request.args:
        group_id_number = str(request.args['group_id'])
    
    if group_id_number == N:
        return "{'token': B85918591859851}" 
        

    else:
         return "This is a message of error" + "<br>" + "<br>" + str(request.args)
        
    
@app.route('/get/Json', methods=['GET'])
def get():
    token_id_number = None
    S =  "B85918591859851" 
    #example, still have to calculate the true value of S
    json_mean_total_cases = {"d_averages": {"Brazil":433891.216981132,"Iran":92607.858490566,"Mexico":75239.5147058823,"Netherlands":24519.1132075472,"Spain":132212.9099526066}}
    
    if 'token_id' in request.args:
        token_id_number = str(request.args['token_id'])
    
    if token_id_number == S:

        return json_mean_total_cases
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