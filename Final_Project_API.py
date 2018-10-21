"""
Creating an API for Eagles and use Python to POST and GET JSON data
--author: Morleh 'soko' Sokargbo
--Created on Sep, 2018
"""
from flask import Flask, render_template, request, jsonify
import eagles

app = Flask(__name__) #creating the object
# @app.route('/')
# def hello():
# 	return "Hello, this databae is about eagles--I mean all kinds of eagles!"

@app.route('/eagle', methods=['POST'])
#post endpoint

def fetch ():
    name = request.get_json()["name"] #parsing the payload
    eagles.names.append(name) #adding new value to list
    #confirming that we wrote it in the list (new list)
    return jsonify(eagles.names)
#why am i getting from the SAME or DIFFERENT client?
#
# def eaglesPictures ():
#     pic = request.get_json()["pic"]
#     eagles.names.append(pic)
#     return jsonify(eagles.names)
#why am i getting from the SAME or DIFFERENT client?

@app.route('/form_input', methods=['POST', 'GET'])

# Function that returns the page: Display "Hello, World!"
def index():
  # return 'Hello, World. Meep Meep!'
  return render_template ("index.html")


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    say=request.form['say']
    to=request.form['to']
    return jsonify({"to":to,"say":say})

@app.route('/seeeagle', methods=['GET'])
def seaeagle():
    return jsonify(eagles.names)

    # eagle = request.get_json()["name"]
    # names.append(eagle)
    # #confirming that we wrote it in the list (new list)
    # return jsonify(names)


if __name__ == '__main__':
    app.run(debug=True)
