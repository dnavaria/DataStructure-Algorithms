def count_factors_of2(A):
    count = 0
    i = 1
    while i * i <= A:
        if A % i == 0:
            count += 1 if i == A // i else 2
        i += 1
    return count


count_factors_of2(24)