def fibonacci(**kwargs):
    n = kwargs.get('n', 10)
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

#exmaples
print(fibonacci(n=5))
print(fibonacci(n=10))
print(fibonacci(n=11))
