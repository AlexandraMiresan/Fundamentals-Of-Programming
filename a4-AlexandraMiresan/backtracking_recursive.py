# Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n,
# such that between any two numbers on consecutive positions, the difference in absolute value is at least m.
# If there is no solution, display a message.
import colorama
from colorama import Fore

def Ok(k, x, m):
    if k == 0:
        return True
    if abs(x[k] - x[k - 1]) >= m:
        return True
    return False


def Afisare(k, x):
    toPrint = ""
    for i in range(k + 1):
        toPrint += str(x[i]) + " "
    print(Fore.LIGHTMAGENTA_EX + toPrint)


def Back(k, x, n, m, ok):
    if k == len(x):
        return ok
    for i in range(1, n):
        x[k] = i
        if Ok(k, x, m):
            if k > 0:
                Afisare(k, x)
                ok = True
            ok = Back(k + 1, x, n, m, ok)
    return ok


def main():
    colorama.init(autoreset=True)
    try:
        n = int(input("Enter n: "))
        if n <= 0:
            print("Please enter a natural value greater than 0.")
        else:
            m = int(input("Enter m: "))
            if m <= 0:
                print("Please enter a natural value greater than 0.")
            else:
                x = [0] * n
                x[0] = 1
                ok = Back(0, x, n, m, False)
                if not ok:
                    print(Fore.LIGHTYELLOW_EX + "no solution :(")

    except ValueError:
        print(Fore.RED + "ERROR!Please enter a natural number")


if __name__ == '__main__':
    main()