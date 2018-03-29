import csv
from famersMarket import FamersMarket
from function import get_market_list,dist,get_nearest_markets,get_minimum_traveling_route
data = csv.reader(open("markets.csv"))
ma = get_market_list("markets.csv")
n=get_nearest_markets(-80,50,4,ma)
print(get_minimum_traveling_route(-80, 50, n))