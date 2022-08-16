from warsey import checkpass
import json
import string
import secrets

def createuser(username, password):
    passhash = checkpass.hashthis(password)
    filename = "appdata/users.json"
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data[username] = passhash
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()

def randompass():
    symbols = ['#', '%', '!'] 
    password = ""
    for _ in range(3):
        password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(symbols)
    return password

def deluser(username):
    with open("appdata/users.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data[username] = "deleted"
    with open("appdata/users.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent = 4)

def autocreateuser(username):
    password = randompass()
    createuser(username, password)
    return password

def userpermission_isadmin(user):
    filename = "appdata/userpriv.json"
    with open(filename,'r+') as file:
        file_data = json.load(file)
    array_length = len(file_data)
    try:
        adminrights = file_data[user][0]["isAdmin"]
    except:
        return False
    file.close()
    if adminrights == "True":
        return True
    else:
        return False