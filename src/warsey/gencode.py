import random
import string
import json
import os.path
import hashlib

def genpart(length):
    length_of_string = int(length)
    letters = string.ascii_uppercase
    random_string = ""
    for number in range(length_of_string):
        random_string += random.choice(letters)
    return random_string

def gencode():
    while True:
        code = f"{genpart(4)}-{genpart(6)}-{genpart(4)}"
        codehash = hashlib.md5(code.encode("utf")).hexdigest()
        if os.path.exists(f"appdata/invitecodes/{codehash}.json") == False:
            break
    return code
