import math

class Key:
    def __init__(self, exponent, modulus):
        self.exponent = exponent
        self.modulus = modulus


def create_keys(p: int, q: int):
    n = p * q
    r = (p - 1) * (q - 1) # Eulers totient theorum provides the number of coprimes of n smaller than n.
    e = find_e(n, r) # A number between 2 and r that is coprime with both n and r. This can often be defaulted to 3, 5 or commonly 65537 for large primes.
    d = pow(e, -1, r) # Multiple of e that has a remainder of 1 when divided by r. In this case we will go with the first multiple that satisfies these conditions.

    if d == e: # keys won't be secure if d and e are the same.
        d += r # To resolve this add any multiple of r to d since d will always be one substracted from a multiple of r.

    public_key = Key(e, n)
    private_key = Key(d, n)

    return (public_key, private_key)


def coprime(a, b):
    if math.gcd(a, b) == 1:
        return True

    return False

def find_e(n: int, r: int):
    for i in range(2, r + 1):
        if coprime(i, n) and coprime(i, r):
            return i # In this case just finding the first/smallest number that is coprime to n and r.
        
    raise Exception("There was a problem and no suitable number was found for e.")


def encrypt_or_decrypt(message: int, key: Key):
    return pow(message, key.exponent) % key.modulus


def main():
    public, private = create_keys(2, 7)
    print(f"n = {public.modulus}, e = {public.exponent}, d = {private.exponent}")

    m = 2
    c = encrypt_or_decrypt(m, public)
    decrypted_message = encrypt_or_decrypt(c, private)

    print(f"m = {m}, c = {c}, decrypted message = {decrypted_message}")


if __name__ == "__main__":
    main()
      