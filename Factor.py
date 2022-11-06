def factor(n):
    import itertools, math
    if n <= 1:
        return []
    x = 2
    for cycle in itertools.count(1):
        y = x
        for i in range(1 << cycle):
            x = (x * x + 1) % n
            d = math.gcd(x - y, n)
            if d > 1:
                return [d] + factor(n // d)
print(factor(1111123456789098765432))