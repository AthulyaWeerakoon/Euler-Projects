def factorial(a, b):  # find a!/b!
    if a - 1 == b:
        return a
    else:
        return a * factorial(a - 1, b)


'''
def is_prime(n):
    for i in range(2, n ** (1 / 2) + 1):
        if n % i == 0:
            return False
    return True
'''


def get_prime_factors(n):  # get all prime factors (one factor only counted once)
    m = n
    factors = []
    i = 2
    while m > 1 and i <= n / 2:
        if m % i == 0:
            m /= i
            if len(factors) > 0:
                if factors[-1] != i:
                    factors.append(i)
            else:
                factors.append(i)
        else:
            i += 1

    return factors


def get_common_factors(m, n):  # get common prime factors of two numbers
    f = [get_prime_factors(m), get_prime_factors(n)]
    factors = []
    for a in f[0]:
        for i, b in enumerate(f[1]):
            if a == b:
                factors.append(b)
                f[1].pop(i)

    return factors


def combine(a, n):  # return all the possible combinations of 'n' number of terms of 'a' multiplied by each other
    if len(a) == n:  # base case
        _return = 1
        for j in a:
            _return *= j
        return [_return]
    elif n == 1:
        return a
    else:  # recursive case
        _return = []
        for i in range(len(a) - n + 1):
            b = []
            for j in combine(a[i + 1: len(a)], n - 1):
                b.append(a[i] * j)
            _return += b
        return _return


def required_combinations(m, n):  # get all the sets of required combinations
    factors = get_common_factors(m, n)
    combinations = []
    for i in range(1, len(factors) + 1):
        combinations.append(combine(factors, i))
    return combinations


def count_for_each_division(n, m, d):  # number of candle arrangements per each count of divisions
    j = n // d
    k = n // d - m // d if n // d - m // d > m // d else m // d
    l = n // d - m // d if n // d - m // d < m // d else m // d
    return factorial(j, k) // (factorial(l, 0))  # simplified nCr, requires optimisation through number theory


def f(n, m):
    if n > m:
        terms = []
        for i in required_combinations(n, m):
            terms.append([])
            for j in i:
                terms[-1].append(count_for_each_division(n, m, j))
        # print(terms)
        sum_arrangements = 0
        for i, a in enumerate(terms):
            for b in a:
                if i % 2 == 0:
                    sum_arrangements += b
                else:
                    sum_arrangements -= b

        return sum_arrangements
    else:
        raise ValueError("n should be greater than m")


print(f(360, 20))
