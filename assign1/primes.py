import math
n = input("Compute primes up to?")
n = int(n)
li = []
for i in range(2, n+1):
    boolean = True
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            boolean = False
    if(boolean):
        li.append(i)
for k in range(0, len(li)):
    print(li[k], end=" ")
