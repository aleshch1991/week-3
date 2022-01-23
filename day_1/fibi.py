def fibonacci(n):
    if n<=0:
      return []
    a = 0
    b = 1
    l = [0]
    for i in range(n):
        a,b = b, a+b
        l.append(a)
    return l[0:n]