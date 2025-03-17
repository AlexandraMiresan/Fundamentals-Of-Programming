import random
import colorama
import pyfiglet
from colorama import Fore, Style


def test():
    list_test1 = [1, 2, 3, 4, 5]
    list_test2 = [2, 4, 6, 8, 10]
    list_test3 = [1, 3, 5, 7, 9]
    list_test4 = [2, 1, 5, 4, 3]
    assert binary_search(list_test1, 2, 0, len(list_test1) - 1) == 1
    assert binary_search(list_test2, 6, 0, len(list_test2) - 1) == 2
    assert binary_search(list_test3, 9, 0, len(list_test3) - 1) == 4
    assert bogosort(list_test4, 99999) == [1, 2, 3, 4, 5]
    assert comb_sort(list_test4, 99) == [1, 2, 3, 4, 5]
    assert is_sorted(list_test1) == True


def generate_numbers(n):
    a = []
    for i in range(n):
        a.append(random.randint(0, 1000))

    return a


def binary_search(array, n, low, high):
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == n:
            return mid

        elif array[mid] < n:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# 1st iteration
# def bogosort(n, steps):
#     a = n
#     nsteps = steps
#     while not is_sorted(a):
#        random.shuffle(a)
#        if steps == 1:
#            print(a)
#
#        elif nsteps == steps:
#            print(a)
#            nsteps -= 1
#
#        elif nsteps == 1:
#            nsteps = steps
#
#        else :
#            nsteps -= 1
#
#     return a

def bogosort_steps(list, steps):
    for i in range(steps):
        random.shuffle(list)
        if is_sorted(list):
            return list

    print(list)
    return list


def bogosort(list, steps):
    while not is_sorted(list):
        list = bogosort_steps(list, steps)

    return list


def get_gap(gap):
    gap = (gap * 10) // 13
    if gap < 1:
        return 1

    return gap


def comb_sort(list, steps):
    n = len(list)
    nsteps = steps
    gap = n
    swapped = True
    while gap != 1 or swapped == True:
        gap = get_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                swapped = True
                nsteps -= 1
                if nsteps == 0:
                    print(list)
                    nsteps = steps

    return list


def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False

    return True


def print_menu():
    print()
    print("Here are the options from which you can choose from:")
    print("1. Generate a list of `n` random natural numbers. Generated numbers must be between `0` and `1000`.")
    print("2. Search for an item in the list using the binary search algorithm.")
    print("3. Sort the list using the bogosort algorithm.")
    print("4. Sort the list using the comp sort algorithm.")
    print("0. Exit")
    print()


def main_menu():
    print(pyfiglet.figlet_format("WELCOME ^_^"))
    list = []
    sorted_list = []
    test()
    colorama.init(autoreset=True)

    while True:
        print_menu()
        choice = input(Style.BRIGHT + Fore.MAGENTA + "Choose an option = ")

        match choice:
            case "1":
                try:
                    n = int(input("Enter a natural number: "))
                    if n <= 0:
                        print("Enter a positive value")
                    else:
                        list = generate_numbers(n)
                        print(list)

                except ValueError:
                    print(Fore.RED + "ERROR!Please enter a natural number")

            case "2":
                if not list:
                    print("Generate a list first")

                elif not sorted_list:
                    print("The list must be sorted first")

                else:
                    try:
                        x = int(input("Enter a number: "))
                        result = binary_search(sorted_list, x, 0, n - 1)
                        if result == -1:
                            print("Sorry, that number is not in the list")
                        else:
                            print("The number's position in the list is=", result)

                    except ValueError:
                        print(Fore.RED + "ERROR!Please enter a number")

            case "3":
                try:
                    steps = int(input("Please enter a number of steps: "))
                    if steps <= 0:
                        print("Please enter a positive value")
                    else:
                        sorted_list = bogosort(list, steps)
                        print(sorted_list)
                except ValueError:
                    print(Fore.RED + "ERROR!Please enter a natural number")

            case "4":
                try:
                    steps = int(input("Please enter a number of steps: "))
                    if steps <= 0:
                        print("Please enter a positive value")
                    else:
                        sorted_list = comb_sort(list, steps)
                        print(sorted_list)
                except ValueError:
                    print(Fore.RED + "ERROR!Please enter a natural number")

            case "0":
                break

            case default:
                print("Please enter a valid option.")


if __name__ == "__main__":
    main_menu()
