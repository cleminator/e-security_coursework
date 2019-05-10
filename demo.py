from pypresent import Present

#Test vectors according to researchers:
plain1 = "0000000000000000".decode('hex')
key1 = "00000000000000000000".decode('hex')
plain2 = "0000000000000000".decode('hex')
key2 = "ffffffffffffffffffff".decode('hex')
plain3 = "ffffffffffffffff".decode('hex')
key3 = "00000000000000000000".decode('hex')
plain4 = "ffffffffffffffff".decode('hex')
key4 = "ffffffffffffffffffff".decode('hex')

print Present(key1).encrypt(plain1).encode('hex')
print Present(key2).encrypt(plain2).encode('hex')
print Present(key3).encrypt(plain3).encode('hex')
print Present(key4).encrypt(plain4).encode('hex')
# -> Test vectors successful

# Sample encryption and decryption:
plain = "Plaintxt"
key = "0123456789abcdef0123".decode('hex')

encrypted = Present(key).encrypt(plain)
decrypted = Present(key).decrypt(encrypted)
print plain, decrypted