def Fib1(num):
    fib = [1, 1]
    for i in range(2,num):
        n = fib[i-1] + fib[i-2]
        fib.append(n)
    return fib[num - 1]
def Fib2(num):
    if num > 2:
        return Fib2(num-1)+Fib2(num-2)
    else:
        return 1
print(Fib1(30))
print(Fib2(30))