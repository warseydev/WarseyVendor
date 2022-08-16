from warsey import checkpass
import hashlib

def createuser():
    user = input("Username> ")
    password = input("Password> ")
    data = {user: checkpass.hashthis(password)}
    print(data)

def getcodeinfo():
    code = input("Code> ")
    codehash = hashlib.md5(code.encode("utf")).hexdigest()
    print(f"appdata/invitecodes/{codehash}.json")

createuser()