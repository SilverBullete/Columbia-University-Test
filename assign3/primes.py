import math
def rem(n):
    l = list(range(2, int(math.sqrt(n)+1)))
    return list(map(lambda x,y: y % x, l, [n]*len(l)))
def is_primes(n):
    return 0 not in rem(n)
n = input("Compute primes up to?")
n = int(n)
print(list(filter(is_primes,range(2,n+1))))