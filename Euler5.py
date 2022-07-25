factorized = []
number_in_check = 1
while number_in_check <= 20:
    number = number_in_check
    for i in factorized:
        if number % i == 0:
            number = int(number / i)
    if number > 1:
        factorized.append(number)
    number_in_check += 1
smallest_number = 1
for a in factorized:
    smallest_number = smallest_number * a

print(smallest_number)
