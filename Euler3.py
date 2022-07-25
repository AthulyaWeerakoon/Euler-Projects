divider = 2
number = 600851475143
while number > 1:                                   # first method
    while number % divider != 0:
        divider += 1
    number = number / divider

print(divider)

num = 600851475143

i = 2
while i < num//2:                                   # second method / first, but longer and confusing lol
    is_prime = False
    if num % i == 0:
        other_factor = num // i
        for j in range(2, other_factor//2):
            if other_factor % j == 0:
                i = i * j - 1
                break
            if j == other_factor//2 - 1:
                is_prime = True
    if is_prime:
        print(num // i)
        break
    i += 1


def largest_prime_factor(a):                                    # using recursion
    for small_factor in range(2,  a // 2 + 1):
        if a % small_factor == 0:
            return largest_prime_factor(a // small_factor)
        if small_factor == a // 2:
            return a


print(largest_prime_factor(num))