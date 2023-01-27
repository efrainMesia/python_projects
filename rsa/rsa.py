import random
die = random.SystemRandom()
length_key = 128
probably_prime = True
composite = False
def gcd_euclides(x, y):
    """ Euclides theorem to find GCD of (x,y)

    Args:
        x (int): Number
        y (int): Number 2

    Returns:
        int: GCD of (x,y)
    """
    if y == 0:
        return x
    return gcd_euclides(y, x % y) 


def multiplicative_inverse(mod ,b):
    a = mod
    b_0 = b
    t_0 = 0
    t = 1
    q = a // b_0
    r = a - (q * b_0)
    while r > 0:
        temp = (t_0 - q*t) % mod
        t_0 = t
        t = temp
        a = b_0
        b_0 = r
        q = a // b_0
        r = a - (q * b_0)
    if b_0 != 1:
        print(f"{b} has no inverse modulo {mod}")
        return -1
    return t
     

"""let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
repeat k times:
a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
x ← ad mod n
repeat s times:
    y ← x2 mod n
    if y = 1 and x ≠ 1 and x ≠ n − 1 then  # nontrivial square root of 1 modulo n
        return (“multiple of”, gcd(x − 1, n))
    x ← y
if y ≠ 1 then
    return “composite”
return “probably prime”
"""
def prime_test(n:int):
    """Implementation of Miller Rabin Algorithm

    Args:
        n (int): _description_
        k (int): _description_
    """
    d = n -1 
    s = 0
    while not d & 1:
        d >>= 1
        s = s + 1
    a = die.randrange(2, n-2)
    x = pow(a, d, n)
    y = 0
    for _ in range(s):
        y = pow(x, 2, n)
        #print(f"a= {a}, d= {d}, x= {x}, x^2 ={pow(x,2)}, x^2 mod {n} = {y}")
        if y == 1 and x != 1 and x!= n-1:
            return f"multiple of {gcd_euclides(x-1, n)}"
        x = y
    return y


def miller_rabin(x, k=40):
    if x <=4:
        raise ValueError("x must be bigger than 4")
    results = []
    for _ in range(k):
        results.append(prime_test(x))
    if all( True if res ==1 else False for res in results):
        return True
    return False


def gen_prime(bits):
    while True:
        # making sure x is always odd
        x = (die.randrange(1 << bits - 1, 1 << bits) << 1) + 1
        if miller_rabin(x):
            return x


def rsa():
    p = gen_prime(length_key)
    q = gen_prime(length_key)
    print(f"p = {p}, q= {q}")
    while p == q:
        p = gen_prime(length_key)
        q = gen_prime(length_key)
    n = p*q
    phy_n = (p - 1) * (q - 1)

    b = die.randrange(1, phy_n)
    while gcd_euclides(b, phy_n) != 1:
        b = die.randrange(1, phy_n)
    a = multiplicative_inverse(phy_n, b)

    print(f"public key = ({n},{b})")
    print(f"private key = ({p},{q},{a})")


rsa()