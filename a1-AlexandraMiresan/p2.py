# Solve the problem from the second set here
#Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n.
#Two prime numbers p and q are called twin if q - p = 2.
#from math import sqrt
from p1 import is_prime

def test():
    assert twin_primes(8) == (11, 13)
    assert twin_primes(15) == (17, 19)

# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(sqrt(n))+1, 2):
#         if n % i == 0:
#             return False
#
#     return True

def twin_primes(n : int):
    ok = False
    p1 = n + 1
    while not ok:
     while not is_prime(p1):
        p1 += 1

     p2 = p1 + 2
     if is_prime(p2):
         ok = True

     else:
         p1 += 1

    return p1, p2


def main():
    test()
    try:
         n = int(input("Enter a non-null natural number:"))
         twins = twin_primes(n) #here a tuple is returned
         print(twins[0], twins[1]) #we access the elements of the tuple by their indexes


    except ValueError:
         print("Please enter a non-null natural number")

if __name__ == '__main__':
    main()