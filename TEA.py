# TEA (Tiny Encryption Algorithm) Pythonda
def shifrlash(v, kalit):
    v0, v1 = v[0], v[1]
    k0, k1, k2, k3 = kalit[0], kalit[1], kalit[2], kalit[3]
    delta = 0x9E3779B9
    yigindi = 0

    for _ in range(32):
        yigindi += delta
        v0 += ((v1 << 4) + k0) ^ (v1 + yigindi) ^ ((v1 >> 5) + k1)
        v1 += ((v0 << 4) + k2) ^ (v0 + yigindi) ^ ((v0 >> 5) + k3)

    return v0, v1

def shifrdan_chiqarish(v, kalit):
    v0, v1 = v[0], v[1]
    k0, k1, k2, k3 = kalit[0], kalit[1], kalit[2], kalit[3]
    delta = 0x9E3779B9
    yigindi = delta * 32

    for _ in range(32):
        v1 -= ((v0 << 4) + k2) ^ (v0 + yigindi) ^ ((v0 >> 5) + k3)
        v0 -= ((v1 << 4) + k0) ^ (v1 + yigindi) ^ ((v1 >> 5) + k1)
        yigindi -= delta

    return v0, v1

plaintext = (0x12345678, 0x9ABCDEF0)
kalit = (0x0A0B0C0D, 0x0E0F1011, 0x12131415, 0x16171819)

shifrlangan_matn = shifrlash(plaintext, kalit)
print(f"Shifrlangan matn: {shifrlangan_matn}")

chiqarilgan_matn = shifrdan_chiqarish(shifrlangan_matn, kalit)
print(f"Shifrdan chiqarilgan matn: {chiqarilgan_matn}")
