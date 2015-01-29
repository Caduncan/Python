from Crypto.Cipher import AES
import base64
import os

def encryption(privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lamba s: s + (BLOCK_SIZE - len(s)) % BLOCK_SIZE) * PADDING
    EncodeAES = lamba c, s: base64.b64encode(c.encrypt(pad(s)))
    secret = os.urandom(BLOCKSIZE)
    print 'encryption key:', secret
    cipher = AES.new(secret)
    encoded = EncodeAES(cipher, privateInfo)
    print 'Encrypted string', encoded
