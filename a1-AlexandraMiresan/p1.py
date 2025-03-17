# Solve the problem from the first set here
#Generate the first prime number larger than a given natural number n.

from math import sqrt

def test():
    assert largest_prime(4) == 5
    assert largest_prime(7) == 11
    assert largest_prime(14) == 17

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range (3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def largest_prime(n: int):
    j = n + 1
    while not is_prime(j):
         j += 1
    return j

def main():
    test()
    try:
         n = int(input("Enter a integer number:"))
         print(largest_prime(n))
    except ValueError:
        print("Please enter a natural number")



if __name__ == '__main__':
    main()