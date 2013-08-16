from Flask-RequireJSON import requires_json
from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=['POST'])
@requires_json(required=['email', 'password'])
def login():

    # Safely get required values from json with errors

    email = request.json['email']
    password = request.json['password']

    if email and password:
        return jsonify({"message": "Woohoo, User " + email + " successfully logged in"})
    else:
        return jsonify({"message": "Username or password was incorrect" })


@app.route("/user/<int:uid>", methods=['GET', 'PATCH', 'DELETE' ])
@requires_json(required=['api_key'], ignore=['DELETE'])
def editUser(uid):

    # Ignore methods which may not require json being sent.
    # GET is ignored by default

    api_key = request.json['api_key']

    if request.method == 'GET':
        return uid
    if request.method == 'DELETE':
        # Delte user from DB
        return jsonify({"message": "User succesfully deleted"})
    if request.method == 'PATCH':
        # Update user
        return jsonify({ "message": "User updated" })
 

if __name__ == "__main__":
    app.run()
