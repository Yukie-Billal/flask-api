import json
import os
from validator import validate

user_dict_template = {
    "nama" : "",
    "email" : "",
    "umur" : 8
}

def loadUser(res = False) :
    try:
        with open('data/user.json', mode='r') as user_json : 
            users = user_json.read()
    except Exception as e:
        print(e)
        os.system('mkdir data')
        os.system('touch data/user.json')
        with open('data/user.json', mode='w') as user_json : 
            user_json.write('{}')
        with open('data/user.json', mode='r') as user_json : 
            users = user_json.read()

    print(res)
    if res:
        return response(users, "Get all")
    return json.loads(users)

def setId(user, data_users) :
    if len(data_users) > 0:
        for id in data_users : 
            last_id = int(id)
    else :
        last_id = 0

    data_users[f"{last_id+1}"] = user
    user_with_id = {
        f"{last_id+1}" : user
    }
    return user_with_id, data_users

def saveUsers(users: dict) :
    with open("data/user.json", mode='w') as file :
        result = file.write(json.dumps(users))
        return result

def add(request) :
    users = loadUser()
    data_user = json.loads(request.data)

    # Add req user to user.json
    result, validate_user, error_message = request_validation(data_user)
    if result : 
        user, new_users = setId(validate_user, users)
        saveUsers(users)
        return True, response(user, 'Add success')

    else :
        return False, response(none, 'Something wrong', 400, error_message)

def edit(request, id) :
    users = loadUser()
    data_user = json.loads(request.data)

    result,validate_user,error_message = request_validation(data_user)
    if result :
        id = str(id)
        users[id] = validate_user
        saveUsers(users)
        return True, response({id : validate_user}, "Edit success")
    else : 
        return False, response(none, 'Something wrong', 400, error_message)


def delete(id) :
    users = loadUser()

    # validation
    rules = {"id":"required|integer"}
    req = {"id":id }
    result, user,_ = validate(req, rules, return_info=True)
    if result : 
        print(user)
        # delete data user by id
        del users[str(id)]
        saveUsers(users)

        return True, response(user, "Delete success")
    return False, response(none, "id doesn't match", 400, error={"message" : "id doesn't match"})

def request_validation(user:dict) -> bool:
    rules = {
        "nama" : "required",
        "email" : "required|mail",
        "umur" : "integer|min:8",
    }
    
    result, data, message = validate(user, rules, return_info=True)
    return result, data, message

def response(data, msg, status = 200, error = None) :
    res = {
        "flaskapi" : {
            "status" : status,
            "message" : msg,
            "results" : data,
            "error" : error
        }
    }
    return res