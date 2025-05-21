def factorial(*args):
    results = []
    for n in args:
        if n < 0:
            results.append(None)
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            results.append(result)
    return results

#examples
print(factorial(5))
print(factorial(0, 3, 7))
print(factorial(-1))
