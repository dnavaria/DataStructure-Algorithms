def perfect_number(A):
    count = 0
    i = 1
    while i * i <= A:
        if i * i == A:
            return i
        i += 1
    return -1


perfect_number(25)
