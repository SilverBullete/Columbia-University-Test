import csv
import sys
def args(cs):
    import csv
    data = csv.reader(open(cs))
    l = []
    for i in data:
        if i[4] == "city":
            continue
        l.append(i[4])
    l = list(set(l))
    a = {}
    b = {}
    data = csv.reader(open(cs))
    for i in data:
        if i[7] == "" or i[7] == "zip":
            continue
        a[i[7]] = tuple(i)
    for i in range(0, len(l)):
        b[l[i]] = set()
    data = csv.reader(open(cs))
    for i in data:
        for k in range(0, len(l)):
            if i[4] == l[k]:
                b[l[k]].add(i[7])
    return a, b
def info( name,address,state , city, zip):
    return "%s\n%s %s,%s\n%s"%(name,address,city,state,zip)
csv = sys.argv[1]
result_a, result_b = args(csv)
while True:
    n = input("请输入一个邮政编码或城市名(输入quit退出)：")
    if n == "quit":
        break
    if n in result_a:
        print(info(result_a[n][1],result_a[n][3],result_a[n][4],result_a[n][6],result_a[n][7]))
    elif n in result_b:
        l = list(result_b[n])
        for i in range(0,len(l)):
            if l[i] != "":
                print(info(result_a[l[i]][1], result_a[l[i]][3], result_a[l[i]][4],
                       result_a[l[i]][6], result_a[l[i]][7]))
    else:
        print("请输入正确的邮政编码或城市名")
