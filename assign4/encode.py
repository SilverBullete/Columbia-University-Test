from gen_key import Key
def encode(str,key):
    li = []
    for i in range(0,len(str)):
        n = key[str[i]]
        li.append(['a']*n)
    return li