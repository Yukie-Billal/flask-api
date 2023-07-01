from .. import app
# import json
import requests

@app.route('/home')
def home() :
    r = requests.get('http://localhost:5000')
    user = r.json()
    return user