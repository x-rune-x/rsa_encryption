class Key:
    def __init__(self, exponent, modulus):
        self.exponent = exponent
        self.modulus = modulus


def create_keys(p: int, q: int):
    n = p * q # modulus
    r = (p - 1) * (q - 1) # Eulers totient theoraum provides the number of coprimes of n smaller than n.
    e = max([x for x in range(1, r + 1) if coprime(x, n) and coprime(x, r)]) # Largest number between 1 and r that is coprime with both n and r.
    d = pow(e, -1, r) # Lowest multiple of e that has a remainder of 1 when divided by r.

    if d == e: # keys won't be secure if d and e are the same (happens if p, q are 3, 7). To resolve this add any multiple of r to d since d will always be one substracted from a multiple of r.
        d += r

    public_key = Key(e, n)
    private_key = Key(d, n)

    return (public_key, private_key)


def find_greates_common_denominator(a, b):
    # Everything divides 0 
    if (a == 0 or b == 0): return 0
    
    # base case
    if (a == b): return a
    
    if (a > b): 
        return find_greates_common_denominator(a - b, b)
            
    return find_greates_common_denominator(a, b - a)

 
def coprime(a, b):    
    if ( find_greates_common_denominator(a, b) == 1): # if the gcd of two numbers is 1 then they are coprime
        return True

    return False 


def main():
    public, private = create_keys(2, 7)

    print(f"n = {public.modulus}, e = {public.exponent}, d = {private.exponent}")


if __name__ == "__main__":
    main()
    