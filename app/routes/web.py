from .. import app

@app.route('/home')
def home() :
    # user = requests.get("http://localhost:5000")
    return "user"