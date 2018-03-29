from gen_key import Key
from decode import decode
import pickle
f1 = open("Key.txt", "rb")
key = pickle.load(f1)
f2 = open("encode.txt","rb")
encode = pickle.load(f2)
print(decode(encode,key))