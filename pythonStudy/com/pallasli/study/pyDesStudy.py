'''
Created on 2016年3月24日

@author: lyt
'''
import base64
from pyDes import *

Des_Key = "BHC#@*UM" # Key
# Des_IV = "\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量
Des_IV = "\1\1\1\1\1\1\1\1" # 自定IV向量

def DesEncrypt(str):
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
#     k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    EncryptStr = k.encrypt(str)

    return base64.b64encode(EncryptStr) #转base64编码返回
def DesDecrypt(str):
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
#     k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    DecryptStr = base64.b64decode(str)

    return k.decrypt(DecryptStr) #转base64编码返回
print(DesEncrypt("李永涛".encode(encoding='utf_8', errors='strict')))
print(DesDecrypt("klfyO4qzH49QC7LMUadnow==" ).decode(encoding='utf_8', errors='strict'))

data = "Please encrypt my data"
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
print ("Decrypted: %r" % k.decrypt(d, padmode=PAD_PKCS5))
assert  k.decrypt(d, padmode=PAD_PKCS5).decode(encoding='utf_8', errors='strict') == data