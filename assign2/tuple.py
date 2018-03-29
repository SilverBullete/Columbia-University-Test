def zip(li1,li2):
    li3 = []
    if len(li1)==len(li2):
        for i in range(0,len(li1)):
            li3.append((li1[i],li2[i]))
        return li3
    else:
        return '两个数组长度不一致'
def unzip(li):
    li1 = []
    li2 = []
    for i in range (0,len(li)):
        li1.append(li[i][0])
        li2.append(li[i][1])
    return (li1,li2)
