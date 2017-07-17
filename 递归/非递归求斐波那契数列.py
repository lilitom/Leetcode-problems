def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
    return b
print fab(5)