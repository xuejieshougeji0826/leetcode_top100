def Fibonacci(n):
    max =45
    fib =[]
    fib.append(0)
    fib.append(1)
    fib.append(1)
    for i in range(3, max):
        fib.append(fib[-2] + fib[-1])

    return fib[n]
print(Fibonacci(39))
