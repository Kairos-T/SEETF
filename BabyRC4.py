"""
The given code is an implementation of an RC4 encryption oracle. The task is to recover the flag by reverse engineering the encryption process. Let's break down the code step by step:

Two ciphertexts, c0 and c1, are provided in hexadecimal format.
The code XORs c0 and c1 byte by byte to obtain the keystream. The keystream is the result of XORing the corresponding bytes of the two ciphertexts.
The next step XORs the obtained keystream with a sequence of 'a's to recover the key used in the RC4 encryption. The assumption here is that the original plaintext used for c1 was a sequence of 'a's.
The recovered key is then printed as a hexadecimal string.
The code continues by assuming another way of recovering the key. It takes a given hexadecimal representation of the key (recovered_key_hex), decodes it from hexadecimal to bytes, reverses the byte order, and appends 'SE' to the front of the key to create the flag.
Finally, the recovered flag is printed.
"""

import binascii
from Crypto.Cipher import ARC4
from os import urandom

c0 = bytes.fromhex('b99665ef4329b168cc1d672dd51081b719e640286e1b0fb124403cb59ddb3cc74bda4fd85dfc')
c1 = bytes.fromhex('a5c237b6102db668ce467579c702d5af4bec7e7d4c0831e3707438a6a3c818d019d555fc')

# XOR c0 and c1 
keystream = bytes(c0_byte ^ c1_byte for c0_byte, c1_byte in zip(c0, c1))

key = bytes(keystream_byte ^ ord('a') for keystream_byte in keystream)

print("Recovered key:", key.hex())


recovered_key_hex = '7d35333832656661633a733573733579336b5f3443725f33355565725f724576336e7b45'
recovered_key = binascii.unhexlify(recovered_key_hex)
recovered_key = recovered_key[::-1]  # Reverse the key
flag = "SE" + recovered_key.decode('ascii')

print("Flag:", flag)

