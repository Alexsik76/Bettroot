a, b = 1, 1
fib_sum = 0
while b < 40:
    if b % 2 == 0:
        fib_sum += b
    a, b = b, a + b
print(a)
print(b)
print(fib_sum)
