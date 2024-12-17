# Sodda RSA algoritmi
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Kalitlarni yaratish
def generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Ochiq kalit uchun e qiymatini topamiz (e va phi_n o'zaro tub bo'lishi kerak)
    e = 2
    while e < phi_n:
        if gcd(e, phi_n) == 1:
            break
        e += 1

    # Yopiq kalit d qiymatini topamiz
    d = mod_inverse(e, phi_n)

    return (n, e), (n, d)

# Shifrlash funksiyasi
def encrypt(plaintext, public_key):
    n, e = public_key
    encrypted_message = [(ord(char) ** e) % n for char in plaintext]
    return encrypted_message

# Shifrdan chiqarish funksiyasi
def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr((char ** d) % n) for char in encrypted_message])
    return decrypted_message

# Foydalanish
p = 61  # Oddiy tub son
q = 53  # Oddiy tub son

public_key, private_key = generate_keys(p, q)

print("Ochiq kalit:", public_key)
print("Yopiq kalit:", private_key)

matn = input("Shifrlash uchun matn kiriting: ")
encrypted_message = encrypt(matn, public_key)
print("Shifrlangan matn:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Shifrdan chiqarilgan matn:", decrypted_message)
