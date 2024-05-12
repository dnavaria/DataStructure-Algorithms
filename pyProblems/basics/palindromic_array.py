def reverseNumber(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


def PalinArray(arr, n):
    for num in arr:
        if reverseNumber(num) != num:
            return False
    return True


print(PalinArray([111, 222, 333, 444], 4))
