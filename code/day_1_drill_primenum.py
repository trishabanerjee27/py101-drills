def is_prime(*args):
    results = []
    for num in args:
        if num <= 1:
            results.append(False)
        elif num == 2:
            results.append(True)
        elif num % 2 == 0:
            results.append(False)
        else:
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    results.append(False)
                    break
            else:
                results.append(True)
    return results

#examples
print(is_prime(2, 3, 4, 5))
print(is_prime(0, 1, -7))
print(is_prime(29))
