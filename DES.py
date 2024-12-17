
def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def des_round(left, right, round_key):
    new_left = right
    new_right = xor(left, xor(right, round_key))
    return new_left, new_right

def des_encrypt(plaintext, keys):
    left, right = plaintext[:len(plaintext) // 2], plaintext[len(plaintext) // 2:]

    for round_key in keys:
        left, right = des_round(left, right, round_key)

    return left + right

def des_decrypt(ciphertext, keys):
    left, right = ciphertext[:len(ciphertext) // 2], ciphertext[len(ciphertext) // 2:]

    for round_key in reversed(keys):
        right, left = des_round(right, left, round_key)

    return left + right

keys = ['key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8']

plaintext = "aldkflkg"

ciphertext = des_encrypt(plaintext, keys)
print(f"Shifrlangan matn: {ciphertext}")

decrypted_text = des_decrypt(ciphertext, keys)
print(f"Shifrdan chiqarilgan matn: {decrypted_text}")
