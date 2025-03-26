import hashlib
def calculate_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()
data_to_hash = input('Enter a string: ')
hash_value = calculate_sha256(data_to_hash)
print("Giá trị hash SHA-256:", hash_value)
