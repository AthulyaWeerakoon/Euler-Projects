_sum = 0
n_minus_2th_term = 1
n_minus_1th_term = 1
nth_term = 0
while nth_term < 4000000:
    if nth_term % 2 == 0:
        _sum += nth_term
    nth_term = n_minus_1th_term + n_minus_2th_term
    n_minus_2th_term = n_minus_1th_term
    n_minus_1th_term = nth_term
print(_sum)
