import json
import validator

user = open('data/user.json', mode='r')
users = user.read()

def loadUser() :
    return json.loads(users)

def add(request) :
    user = "data user"
    return True, user

def edit(request, id) :
    user = "Data user"
    return True, user

def delete(id) :
    user = "Data user"
    return True, id

def request_validation(user:dict) -> bool:
    rules = {
        "nama" : "required",
        "nohp" : "required|int|min:8",
        "umur" : "required|int|min:1",
    }
    
    result = validator.validate(user, rules, return_info=True)
    if result : 
        return True
    else :
        return False