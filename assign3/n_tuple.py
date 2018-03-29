def zip(li):
    l = []
    for i in range(0,len(li[0])):
        l1 = []
        for j in range(0,len(li)):
            l1.append(li[j][i])
        tup = tuple(l1)
        l.append(tup)
    return l
def unzip(li):
    l = []
    for i in range(0, len(li[0])):
        l1 = []
        for j in range(0, len(li)):
            l1.append(li[j][i])
        l.append(l1)
    return tuple(l)
print(zip([[1,2,3],[4,5,6],[7,8,9]]))
print(unzip([(1, 4, 7), (2, 5, 8), (3, 6, 9)]))