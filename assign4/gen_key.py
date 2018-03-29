import random
class Key(dict):
    def __init__(self):
        select_list = range(0, 27)
        li = random.sample(select_list,27)
        for i in range(0,len(li)-1):
            self[chr(i+65)] = li[i]
        self[" "] = li[26]
