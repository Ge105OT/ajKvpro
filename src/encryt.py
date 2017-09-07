# -*- coding:utf-8 -*-
import math
import hashlib   
import base64
from Crypto.Cipher import AES

def md5enc(data):
    m2 = hashlib.md5()   
    m2.update(data)   
    return m2.hexdigest()

def parse_hex(hex_str):
    l = int(math.ceil(len(hex_str) / 2))
    buf = ''
    for i in range(0,l):
        s = hex_str[(i * 2) : ((i + 1) * 2)]
        buf = buf + chr(int(s, 16))
    return buf

def iv_create(data):
    ivmd5 = md5enc(data)
    iv = parse_hex(ivmd5)
    return iv
 
def Aes_encrypt(data, password, iv):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(data))
    data = iv + data
    return base64.b64encode(data)
 
def Aes_decrypt(data, password, iv):
    data = base64.b64decode(data)
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s : s[0:-ord(s[-1])]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return data
 
if __name__ == '__main__':
    data = 'd437814d9185a290af20514d9341b710'
    password = '78f40f2c57eee727a4be179049cecf89' #16,24,32位长的密码
    iv = iv_create('78f40f2c57eee727a4be179049cecf89')
    encrypt_data = Aes_encrypt(data, password, iv)
    print 'encrypt_data:', encrypt_data
 
 
    decrypt_data = Aes_decrypt(encrypt_data, password, iv)
    print 'decrypt_data:', decrypt_data