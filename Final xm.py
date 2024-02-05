1    def fib_rec(n):
2        if n == 1:
3            return [0]
4        elif n == 2:
5            return [0,1]
6        else:
7            x = fib_rec(n-1)
8            # the new element the sum of the last two elements
9            x.append(sum(x[:-3:-1]))
10            return x
11    x=fib_rec(5)
12    print(x)