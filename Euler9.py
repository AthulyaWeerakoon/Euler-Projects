num = 1000

for s in range(2, num // 2 + 1):
    if num % s == 0:
        t = num // s - s
        if 0 < t < s:
            print('a = ', s*t)
            print('b = ', (s**2 - t**2) // 2)
            print('c = ', (s**2 + t**2) // 2)
            break


