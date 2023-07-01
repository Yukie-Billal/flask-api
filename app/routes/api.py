from .. import app
from flask import request
from ..controllers import UserController as user
import json

@app.route('/')
def users():
    return user.loadUser()

@app.route('/users', methods=['GET','POST'])
def add_user():
    if request.method == 'POST' : 
        result, data = user.add(request)
        # if result : 
        return data

        
@app.route('/users/<int:id>', methods=['POST'])
def edit_user(id) :
    if request.method == 'POST' :
        print(request.form)
        _,data = user.edit(request, id)
        return data
    
@app.route('/users/<int:id>/delete')
def delete_user(id) :
    _,data = user.delete(id)
    return data