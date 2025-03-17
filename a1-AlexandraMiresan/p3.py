# Solve the problem from the third set here
# Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed.
# A number is perfect if it is equal to the sum of its divisors, except itself.

def test():
    assert perfect_exists(40) == 28
    assert perfect_exists(7) == 6
    assert perfect_exists(8) == 6
    assert perfect_exists(2) == 0

def divisor_sum(n):
    sum = 0
    for i in range(1, n - 1):
        if n % i == 0:
            sum += i

    return sum

def perfect_exists(n):
    ok = False
    i = n - 1

    while not ok and i >= 1:
        if divisor_sum(i) == i:
            ok = True
        else:
            i -= 1

    return i


def main():
    test()
    try:
        n = int(input("Enter a natural number:"))
        perf = perfect_exists(n)
        if perf != 0:
            print(perf)

        else:
            print("Such a value does not exist")


    except ValueError:
        print("Please enter a natural number")



if __name__ == '__main__':
    main()

