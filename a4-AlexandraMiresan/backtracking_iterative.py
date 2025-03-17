# Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n,
# such that between any two numbers on consecutive positions, the difference in absolute value is at least m.
# If there is no solution, display a message.
import colorama
from colorama import Fore
from backtracking_recursive import Ok


def Afisare(k, x):
    toPrint = ""
    for i in range(k):
        toPrint += str(x[i]) + " "
    print(Fore.LIGHTMAGENTA_EX + toPrint)


def Back(x, n, m):
    ok = False
    executionList = []
    executionList.insert(0, (x, 0))
    while not executionList == []:
        toExecute, index = executionList.pop(0)
        if index > 1:
            ok = True
            Afisare(index, toExecute)
        if index != n:
            for i in range(n - 1, 0, -1):
                toExecute[index] = i
                if Ok(index, toExecute, m):
                    executionList.insert(0, (toExecute.copy(), index + 1))
    if not ok:
        print(Fore.LIGHTYELLOW_EX + "no solution :(")


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
                Back(x, n, m)
    except ValueError:
        print(Fore.RED + "ERROR!Please enter a natural value.")



if __name__ == '__main__':
    main()