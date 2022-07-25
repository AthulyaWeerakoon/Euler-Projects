number = 14
three = 3
five = 5
_sum = 0
while three < number:
    if three % 5 != 0:
        _sum += three
    three += 3
while five < number:
    _sum += five
    five += 5
print(_sum)
