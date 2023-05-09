import hashlib

def hash_text(text):
    sha512 = hashlib.sha512(text.encode()).hexdigest()
    sha256 = hashlib.sha256(text.encode()).hexdigest()
    md5 = hashlib.md5(text.encode()).hexdigest()
    md1 = hashlib.new('mdc2', text.encode()).hexdigest()
    
    return {'SHA512': sha512, 'SHA256': sha256, 'MD5': md5, 'MD1': md1}

text = input("Enter the text to hash :D: ")
hashed_text = hash_text(text)
print(hashed_text)
print("Ohh, how much! :D")