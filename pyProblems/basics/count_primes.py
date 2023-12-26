def is_prime(A):
    count = 0
    i = 1
    while i * i <= A:
        if A % i == 0:
            count += 1 if i == A // i else 2
        i += 1
    return 1 if count == 2 else 0


def count_of_primes(A):
    count = 0
    i = 2
    while i <= A:
        if is_prime(i):
            count += 1
        i += 1
    return count


count_of_primes(50)
