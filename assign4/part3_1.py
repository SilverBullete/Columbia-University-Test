from gen_key import Key
from encode import encode
import pickle
key = Key()
f = open("Key.txt","wb")
pickle.dump(key,f)
