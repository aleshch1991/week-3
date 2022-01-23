


def fib(num):
    if num <=1:
        return 1
    else:
        return fib(num-1)+fib(num-2)


def i_fibinoci(n):
    for i in range (0, n+1):
        print(f"Iteration{i}: {fib(i)}")


fib(5)






