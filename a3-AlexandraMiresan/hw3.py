import random
import colorama
import pyfiglet
from colorama import Fore, Style
import timeit
from texttable import *


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

def already_sorted_data(data_size):
    result = list(range(0, data_size))
    return result

def sorted_in_reverse_data(data_size):
    result = list(range(data_size, 0, -1))
    return result

def random_data(data_size):
    result = list(range(0, data_size))
    random.shuffle(result)
    return result

def millis_interval(start, end):
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return int(millis)

def comb_sort1(list):
    n = len(list)
    gap = n
    swapped = True
    while gap != 1 or swapped == True:
        gap = get_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                swapped = True

    return list

def build_result_table_average_case_bogosort():
    table = Texttable()
    table.add_row(['Term', 'Bogosort'])
    for term in [3, 4, 6, 8, 10]:
        data = random_data(term)
        start_bogo = timeit.default_timer()
        row = bogosort1(data)
        end_bogo = timeit.default_timer()

        table.add_row([term, end_bogo - start_bogo])
    return table

def build_result_table_average_case_combsort():
    table = Texttable()
    table.add_row(['Term', 'Comb Sort'])
    for term in [500, 1000, 2000, 4000, 8000]:
        data = random_data(term)
        start_comb = timeit.default_timer()
        row = comb_sort1(data)
        end_comb = timeit.default_timer()
        table.add_row([term, end_comb - start_comb])
    return table

#TODO fix average case

def build_result_table_worst_case_bogosort():
    table1 = Texttable()
    table1.add_row(['Term', 'Bogosort 1', 'Bogosort 2'])
    for term in [3, 4, 6, 8, 10]:
        data = sorted_in_reverse_data(term)
        start_bogo = timeit.default_timer()
        row = bogosort1(data)
        end_bogo = timeit.default_timer()

        data = sorted_in_reverse_data(term)
        start_bogo2 = timeit.default_timer()
        row = bogosort1(data)
        end_bogo2 = timeit.default_timer()
        table1.add_row([term, end_bogo - start_bogo, end_bogo2 - start_bogo])

    return table1

def build_result_table_worst_case_combsort():
    table2 = Texttable()
    table2.add_row(['Term', 'Comb Sort'])
    for term in [500, 1000, 2000, 4000, 8000]:
        data = sorted_in_reverse_data(term)
        start_comb = timeit.default_timer()
        row = comb_sort1(data)
        end_comb = timeit.default_timer()

        table2.add_row([term, end_comb - start_comb])

    return table2

def build_result_table_best_case_bogosort():
    table = Texttable()
    table.add_row(['Term', 'Bogosort'])
    for term in [3, 4, 6, 8, 10]:
        data = already_sorted_data(term)
        start_bogo = timeit.default_timer()
        row = bogosort1(data)
        end_bogo = timeit.default_timer()

        table.add_row([term, end_bogo - start_bogo])
    return table

def build_result_table_best_case_combsort():
    table = Texttable()
    table.add_row(['Term', 'Comb Sort'])
    for term in [500,1000,2000,4000,8000]:
        data = already_sorted_data(term)
        start_comb = timeit.default_timer()
        row = comb_sort1(data)
        end_comb = timeit.default_timer()
        table.add_row([term, end_comb - start_comb])

    return table



def bogosort1(list):
    n = len(list)
    while not is_sorted(list):
        random.shuffle(list)

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
    print("4. Sort the list using the comb sort algorithm.")
    print("5. Best case")
    print("6. Average case")
    print("7. Worst case")
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

            case "5":
                print(build_result_table_best_case_bogosort().draw())
                print("In the best case of bogosort, the list is already sorted, the time complexity is O(n).")
                print("Because the list is already sorted, the only thing that has to be done is to check all the elements of the list once, one by one.")
                print(build_result_table_best_case_combsort().draw())
                print("Comb Sort's best case is O(n*log n) because, even if the array is nearly sorted or sorted,")
                print("the algorithm still needs multiple passes to shrink to the gap and verify the order. ")
                print("Unlike Bubble Sort, it can't finish in O(n) because it continues to reduce the gap logarithmically, requiring extra checks")


            case "6":
                print(build_result_table_average_case_bogosort().draw())
                print("The average case of Bogosort is O(n * n!) because the algorithm randomly shuffles the array and checks if it is sorted.")
                print("With n! possible permutations of n elements, the expected number of shuffles required to find the sorted order is n!,")
                print("and each check for sorting takes O(n) time, leading to an average case of O(n * n!)")
                print(build_result_table_average_case_combsort().draw())
                print("The average case time complexity of Comb Sort is O(n * log n) because the algorithm reduces the gap between compared elements exponentially with each pass.")
                print("This allows for effective element movement towards their correct positions, resulting in fewer total comparisons. Each pass requires O(n) comparisons, ")
                print("and the logarithmic reduction in gap size leads to and average of log(n) passes, yielding O(n * log n) overall.")

            case "7":
                print(build_result_table_worst_case_bogosort().draw())
                print("In the worst case of bogosort, the complexity is O(infinity). ")
                print("Because this algorithm works by shuffling the list until sorted, there is no guarantee that it will get shuffled in the correct order.")
                print("We can observe in the table above how much the results can vary for the same amount of values.")
                print("Here it does not matter what order the list is in, be it reverse or just a random order, as long as it is not already sorted. ")
                print(build_result_table_worst_case_combsort().draw())
                print("Worst case for Comb Sort is O(n^2) because, like Bubble Sort, it eventually reduces the gap to 1, making it similar to a simple bubble sort.")
                print("In highly unordered arrays, like the ones we are using for example here, which are sorted in reverse order, multiple passes are needed to move elements, leading to quadratic time.")

            case "0":
                break

            case default:
                print("Please enter a valid option.")


if __name__ == "__main__":
    main_menu()
