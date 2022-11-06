import datetime, numpy as np, gmpy2, random, math
random.seed(0)

def num(n):
    return gmpy2.mpz(n)
    
zero, one = num(0), num(1)

def gcd(a, b):
    while b != zero:
        a, b = b, a % b
    return a

def pollard_rho_v0(n):
    f = lambda z: z * z + one
    n, x, y, d, c, t = num(n), one, one, one, 0, datetime.datetime.now()
    while d == one:
        c += 1
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(y - x, n)
    return d, {'i': c, 'n_bits': n.bit_length(), 'd_bits': round(math.log(d) / math.log(2), 2),
        'pow': round(math.log(max(c, 1)) / math.log(d), 4), 'time': str(datetime.datetime.now() - t)}
    
def is_fermat_prp(n, trials = 32):
    n = num(n)
    for i in range(trials):
        a = num((3, 5, 7)[i] if i < 3 else random.randint(2, n - 2))
        if pow(a, n - 1, n) != 1:
            return False
    return True