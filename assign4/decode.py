def decode(li, key):
    str = ""
    for i in range(0,len(li)):
        n = len(li[i])
        a = list(key.keys())[list(key.values()).index(n)]
        str += a
    return str