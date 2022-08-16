from warsey import checkpass, gencode, datahandler, users
import json, hashlib
from datetime import datetime

def timenow():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def userexists(user):
    with open('appdata/users.json', 'r') as file:
        jsondb = json.load(file)
    if user in jsondb:
        file.close()
        return True
    else:
        file.close()
        return False

def userpass(user, password):
    with open('appdata/users.json', 'r') as file:
        jsondb = json.load(file)
    try:
        passhash = jsondb[user]
    except:
        return False
    if passhash == "deleted":
        return False
    elif checkpass.checkhash(password, passhash):
        return True
    else:
        return False

def generatecode(data):
    code = gencode.gencode()
    codehash = hashlib.md5(code.encode("utf")).hexdigest()
    out_file = open(f"appdata/invitecodes/{codehash}.json", "w")
    json.dump(data, out_file, indent = 6)
    out_file.close()
    return code

def updateadmindata():
    try:
        datahandler.updatedata()
    except:
        return None

def isadmin(user):
    return users.userpermission_isadmin(user)

def createuser(user):
    return users.autocreateuser(user)

def deleteuser(user):
    users.deluser(user)