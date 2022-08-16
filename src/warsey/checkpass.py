from passlib.hash import sha256_crypt

def hashthis(text):
    return sha256_crypt.hash(text)

def checkhash(text, hash):
    return sha256_crypt.verify(text, hash)
