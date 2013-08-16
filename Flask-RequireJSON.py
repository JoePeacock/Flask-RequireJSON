from flask import request, jsonify

def requires_json(required=[], ignore=[]):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if request.method not in ignore or request.method != 'GET':
                contentType = request.headers['Content-Type'] 
                if contentType != "application/json":
                    ''' Return Error for non application/json type '''
                    return jsonify({"message": "Content-Type is not set to application/json", "success": False})
                else:
                    try:
                        data = request.json
                    except:
                        ''' Return Error for improperly formated json string '''
                        return jsonify({"message": "JSON is formatted incorrectly", "success": False})
                for item in required:
                    if item not in request.json:
                        ''' Return error for required fields '''
                        return jsonify({"message": "Required fields not set", "success": False})
            return f(*args, **kwargs)
        return decorated_function
    return decorator
