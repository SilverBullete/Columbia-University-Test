from famersMarket import FamersMarket
def get_market_list(filename):
    import csv
    data = csv.reader(open(filename))
    l = []
    for i in data:
        if i[0] == 'FMID' or i[8] == "" or i[9] == "":
            continue
        fm = FamersMarket(i[0], i[1], i[2], i[3], i[4], i[7], i[8], i[9])
        l.append(fm)
    return l
def dist(x0, y0, x1, y1):
    import math
    return math.sqrt(abs(x0 - x1) ** 2 + abs(y0 - y1) ** 2)
def get_nearest_markets(x,y,n,market_list):
    l = []
    response = []
    for i in market_list:
        if (i.set_x and i.set_y):
            l.append([dist(x,y,i.x,i.y),i])
    l.sort()
    for j in range(0,n):
        response.append(l[j][1])
    return response
def get_minimum_traveling_route(x, y, n_market_list):
    from itertools import permutations
    l1 = permutations(range(len(n_market_list)), len(n_market_list))
    l = []
    d = []
    for i in l1:
        l2 = []
        for j in i:
            l2.append(n_market_list[j])
        l.append(l2)
    for i in l:
        distance = dist(x,y,i[0].x,i[0].y)
        for j in range(1,len(n_market_list)):
            distance = distance + dist(i[j-1].x,i[j-1].y,i[j].x,i[j].y)
        d.append([distance,i])
    d.sort()
    return d[0][1]
