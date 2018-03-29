from gen_key import Key
from encode import encode
import pickle
f1 = open("encode.txt","wb")
f2 = open("Key.txt","rb")
key = pickle.load(f2)
info = input("请输入明文消息（使用大写字母）：")
secret = encode(info,key)
pickle.dump(secret,f1)