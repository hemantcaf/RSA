import random
import math


# function to generate random primes 'p' & 'q' and calculate 'N' and 'PhiN'
def primeNum():
    # An empty list to store the prime numbers to be generated
    primeArray = []
    for i in range(1, 65535):
        # checking for prime numbers in the range between 2 and the square root of the number being checked.
        if all(i % j != 0 for j in range(2, (int)(math.sqrt(i)) + 1)):
            # the valid prime numbers are added to the list
            primeArray.append(i)
    # randomly choose an index from the list
    index1 = random.randint(0, len(primeArray))
    # store the prime number at that random index to 'p'
    p = primeArray[index1]
    index2 = random.randint(0, len(primeArray))
    q = primeArray[index2]
    # calculate N
    N = p * q
    # Calculate Phi N
    PhiN = (p - 1) * (q - 1)
    print("p =", p)
    print("q =", q)
    print("N =", N)
    print("Phi N =", PhiN)
    # returning Phi N so that it can be called in other functions
    return PhiN


# function to calculate GCD.
def gcd(m, n):
    # recursively checks highest common factor between n and modulo of m & n until it becomes zero or one.
    # If it's zero, then the last value of m is returned. Otherwise, 1 is returned.
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


# function to calculate public key 'e'.
def calc_E():
    # Accepting value of Phi N from primeNum() function
    PhiN = primeNum()
    # Randomly generating public key 'e' between 2 and PhiN
    e = random.randrange(2, PhiN)
    # calculate gcd of 'e' and 'Phi N'
    check = gcd(e, PhiN)
    '''loop to keep generating different values for 'e' until the gcd of 'e' and 'Phi N' becomes 1 
    so that they are co-primes.'''
    while check != 1:
        e = random.randrange(2, PhiN)
        check = gcd(e, PhiN)
    print("E =", e)
    return e, PhiN


# Function to calculate the multiplicative inverse
def mulInverse(g, h):
    # Calculating modulo of 'g' with 'h' to reduce 'g' to a number smaller than 'h'
    g = g % h
    # Loop to implement naive approach to calculate modulo of every factor of g between 1 and 'h' to check its inverse.
    # If the factor generates a modulo of 1 with 'h', then that factor is the inverse, otherwise it's 1.
    for i in range(1, h):
        if (g * i) % h == 1:
            return i
    return 1


# Function to calculate the value for private key 'D'.
def calc_D():
    # Accepting values of e and PhiN from genE() function.
    e, PhiN = calc_E()
    # Calculating the multiplicative inverse of 'e' with PhiN to get the value for private key 'd'.
    d = mulInverse(e, PhiN)
    print("D =", d)


# Driver Code
if __name__ == '__main__':
    calc_D()
