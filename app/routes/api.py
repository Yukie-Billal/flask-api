from .. import app
from flask import request
from ..controllers import UserController as user
import json

@app.route('/')
def users():
    return user.loadUser()

@app.route('/route', methods=['GET','POST'])
def add_user():
    if request.method == 'POST' : 
        user.add(request)
        
@app.route('/users/<int:id>')
def edit_user(id) :
    user.edit(request, id)
    
@app.route('/users/<int:id>/delete')
def delete_user(id) :
    user.delete(id)