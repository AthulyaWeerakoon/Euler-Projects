total = 0
number_one = 1
number_two = 2
while number_one <= 100:
    number_two = number_one + 1
    while number_two <= 100:
        total += number_one*number_two
        number_two += 1
    number_one += 1
total *= 2
print(total)
