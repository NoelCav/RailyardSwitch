from flask import Flask, request, redirect, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/checkstatus')
def checkstat():
    status = request.args.get('currentstatus')

    if status == "Good to Proceed":
        return redirect("/getcommand")
    else:
        return "Switch is not in a proper position"


@app.route('/getcommand')
def opencloseSwitch():
    r = request.args.get("commands")

    if not r:
        return "command not processed"
    else:
        response = jsonify(r)
        if r == "open":
            #open switch using forward and backward (controlside)
            #update status to open
        elif r == "close":
            # open switch using forward and backward (controlside)
            # update status to close
        else:
            #invalid command

        return "request succeeded"



































#import requests

#response = requests.get('http://localhost:8000/') #to request the data from the server to open or close the switch

#status = response.status_code
#.route
#return response as json or html
#battery percentage, switch position

#if status:
#   print("Request has succeeded")
#    print(response.headers)

#else:
#    print("Error:", response.status_code)



