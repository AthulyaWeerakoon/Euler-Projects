a = 9
b = 9
c = 9
found = False
palindrome = 0
while a > 0:
    number_str_1 = str(a)
    while b >= 0:
        number_str_2 = number_str_1 + str(b)
        while c >= 0:
            number_str = number_str_2 + str(c) + str(c) + str(b) + str(a)
            number = int(number_str)
            small_factors = []
            large_factors = []
            divider = 2
            small_factors.append(1)
            large_factors.append(number)
            _continue = False
            while divider < large_factors[len(large_factors) - 1]:
                if number % divider == 0:
                    small_factors.append(divider)
                    large_factors.append(int(number / divider))
                if divider > 1000:
                    _continue = True
                    break
                divider += 1
            c -= 1
            if _continue:
                continue
            if len(str(small_factors[len(small_factors) - 1])) == 3 and len(str(large_factors[len(large_factors) - 1])) == 3:
                found = True
                palindrome = number
                break
        c = 9
        b -= 1
        if found:
            break
    a -= 1
    b = 9
    if found:
        break

print(palindrome)
