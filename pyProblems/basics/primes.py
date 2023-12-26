def is_prime(A):
    count = 0
    i = 1
    while i * i <= A:
        if A % i == 0:
            count += 1 if i == A // i else 2
        i += 1
    return 1 if count == 2 else 0


is_prime(11)
