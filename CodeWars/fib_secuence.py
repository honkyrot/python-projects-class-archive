def productFib(prod):
    a = 0
    b = 1
    c = 0
    while a * b < prod:
        a = b
        b = c
        c = a + b
    return [a, b, a * b == prod]


print(productFib(4895))  # 55, 59, True
