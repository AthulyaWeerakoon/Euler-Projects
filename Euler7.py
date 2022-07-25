def is_prime(a):
    i = 2
    b = str(a)
    last_digits = [0, 2, 4, 5, 6, 8]
    if len(b) > 1:
        for c in last_digits:
            if b[len(b) - 1] == c:
                return False
    while i <= a/2:
        if a % i == 0:
            return False
        i += 1
    return True


num = 2
count = 0
while count <= 10001:
    if is_prime(num):
        count += 1
    num += 1

print(num)
