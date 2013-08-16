# Flask-RequireJSON

### Flask decorator for checking JSON requests in a RESTful API

Flask-RequireJSON takes care of checking the ```Content-Type``` headers, checks the validity of the JSON, and makes sure your required values are set, on the request methods you specify.

#### Setup

Simply use the RequiresJSON.py file, and include it in your app, or copy the code into your uitls or helpers file.

``` python
from RequireJSON import require_json
```

#### Usage

There are two parameters for Flask-RequireJSON which are ``` ignore ``` and ``` required ```.

##### ignore:
A list of methods to ignore check json on, for use on routes with multiple methods. GET requests are always ignored. 

ex: 
``` python 
@require_json(ignore=['DELETE']) 
``` 


##### required:
A list of required keys that need to be set in the json request. 

ex: 
``` python 
@require_json(required=['email', 'password']) 
```

#### Example Method

``` python
@app.route("/user/<int:uid>", methods=['GET', 'PATCH', 'DELETE'])
@require_json(required=['api_key'], ignore=['DELETE'])
def editUser(uid):
    # Your Code Here
    pass
```

