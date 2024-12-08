def sieve_of_eratosthenes(n): # Will find primes smaller than or equal to n.
    is_prime = [True for i in range(n + 1)]

    for i in range(2, n + 1):
        if is_prime[i] is True:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    
    return [x for x in range(2, n + 1) if is_prime[x] is True]

print(sieve_of_eratosthenes(100))
        