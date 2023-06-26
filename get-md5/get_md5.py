import hashlib

def get_md5(text):
    return hashlib.md5(bytes(text,encoding='utf8')).hexdigest()