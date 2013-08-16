from flask import request, jsonify
from functools import wraps

def requires_json(required=[], ignore=[]):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if request.method in ignore or request.method == 'GET':
                return f(*args, **kwargs)
            else:
                contentType = request.headers['Content-Type'] 
                if contentType != "application/json":
                    ''' Return Error for non application/json type '''
                    return jsonify({"message": "Content-Type is not set to application/json" }), 400
                else:
                    try:
                        data = request.json
                    except:
                        ''' Return Error for improperly formated json string '''
                        return jsonify({"message": "JSON is formatted incorrectly" }), 400
                for item in required:
                    if item not in request.json:
                        ''' Return error for required fields '''
                        return jsonify({"message": "Required fields not set: " + item }), 400
            return f(*args, **kwargs)
        return decorated_function
    return decorator
