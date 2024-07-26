numbers = list(range(1, 16))
primes, not_primes = [], []

for num in numbers[1:]:
    for i in range(2, num):
        if not (num % i):
            not_primes.append(num)
            break
    else:
        primes.append(num)

print('Primes:', primes)
print('Not Primes:', not_primes)
