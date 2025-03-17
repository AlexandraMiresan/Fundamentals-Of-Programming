import random
from unittest import case


# Write the implementation for A5 in this file
#

# Test functions

def test_create_complex_numbers():
    assert create_complex_number_list(2, 3) == [2, 3]
    assert create_complex_number_list(65, 0) == [65, 0]
    assert create_complex_number_list(0, 10) == [0, 10]
    assert create_complex_number_dictionary(12, 4) == {12, 4}
    assert create_complex_number_dictionary(0, 10) == {0, 10}
    assert create_complex_number_dictionary(0, 4) == {0, 4}


def test_get_real_and_imaginary_parts():
    assert get_real_part([2, 3]) == 2
    assert get_real_part([0, 8]) == 0
    assert get_real_part([1, 7]) == 1
    assert get_imaginary_part([2, 3]) == 3
    assert get_imaginary_part([0, 8]) == 8
    assert get_imaginary_part([1, 7]) == 7
    assert get_real_part_dictionary({2, 4}) == 2
    assert get_real_part_dictionary({0, 8}) == 0
    assert get_real_part_dictionary({1, 7}) == 1
    assert get_imaginary_part_dictionary({2, 4}) == 4
    assert get_imaginary_part_dictionary({0, 8}) == 8
    assert get_imaginary_part_dictionary({1, 7}) == 7


def test_longest_distinct_subarray():
    assert longest_distinct_subarray([[2, 3], [4, 7], [1, 0], [2, 3], [4, 2]]) == (4, [[4, 7], [1, 0], [2, 3], [4, 2]])
    assert longest_distinct_subarray([]) == (0, [])
    assert longest_distinct_subarray(
        [{'real': 884, 'imaginary': 307}, {'real': -861, 'imaginary': -374}, {'real': 784, 'imaginary': -4},
         {'real': 890, 'imaginary': 785}, {'real': 681, 'imaginary': 893}]) == (4, [{'real': 884, 'imaginary': 307},
                                                                                    {'real': -861, 'imaginary': -374},
                                                                                    {'real': 784, 'imaginary': -4},
                                                                                    {'real': 681, 'imaginary': 893}])


def test_modulo():
    assert modulo([4, 3]) == 5
    assert modulo([6, 8]) == 10
    assert modulo_dictionary([{4, 3}]) == 5
    assert modulo_dictionary([{6, 8}]) == 10


def test_longest_subsequence():
    assert longest_increasing_subsequence_modulo(
        [[375, -250], [-42, 566], [-549, 818], [536, -953], [23, -8], [2, 56]]) == [[375, -250], [-42, 566],
                                                                                    [-549, 818], [536, -953]]
    assert longest_increasing_subsequence_modulo(
        [{'real': -85, 'imaginary': -313}, {'real': -249, 'imaginary': 303}, {'real': -31, 'imaginary': 413},
         {'real': 1, 'imaginary': 2}]) == [{'real': -85, 'imaginary': -313}, {'real': -249, 'imaginary': 303},
                                           {'real': -31, 'imaginary': 413}]


#
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def add_number_to_list(number_list, real_part, imaginary_part):
    complex_number = create_complex_number_list(real_part, imaginary_part)
    add_number_to_list(complex_number, number_list)


def create_complex_number_list(real_part, imaginary_part):
    return [real_part, imaginary_part]


def add_number_to_list(number_list, complex_number):
    number_list.append(complex_number)


def initial_complex_numbers_list(numberList):
    for i in range(1, 11):
        real_part = random.randint(-1000, 1000)
        imaginary_part = random.randint(-1000, 1000)
        complex_number = create_complex_number_list(real_part, imaginary_part)
        numberList.append(complex_number)


def get_real_part(complex_number):
    return complex_number[0]


def get_imaginary_part(complex_number):
    return complex_number[1]


def toString(number):
    number_string = str(number)
    return number_string


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# def add_number_to_dictionary(number_dictionary, complex_number):
#     number_dictionary["complex numbers"] = complex_number


def initial_complex_numbers_dictionary(number_list):
    for i in range(1, 11):
        real_part = random.randint(-1000, 1000)
        imaginary_part = random.randint(-1000, 1000)
        complex_number = create_complex_number_dictionary(real_part, imaginary_part)
        number_list.append(complex_number)


def create_complex_number_dictionary(real_part, imaginary_part):
    return {"real": real_part, "imaginary": imaginary_part}


def get_real_part_dictionary(param):
    return param.get("real")


def get_imaginary_part_dictionary(param):
    return param.get("imaginary")


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# subarray functions

def longest_distinct_subarray(number_list):
    max_length = 0  # we store the longest distinct subarray
    longest_subarray = []  # a list used to store the final longest subarray
    current_subarray = []  # a list used to store the current longest subarray found as we go through the list

    # we check if the number was already added in the subarray
    for end in range(len(number_list)):
        while number_list[end] in current_subarray:
            current_subarray.pop(0)
            # if the number is already in the list we pop it from the list

        # we add the number to the current subarray list
        current_subarray.append(number_list[end])

        if len(current_subarray) > max_length:
            # we check to see if the new current list is longer than the maximum list we have stored,
            # if so the longest_subarray will be equal to the current subarray and we also update the max_length
            max_length = len(current_subarray)
            longest_subarray = current_subarray[:]

    return len(longest_subarray), longest_subarray


# subsequence functions

def longest_increasing_subsequence_modulo(number_list):
    length_of_number_list = len(number_list)  # stores the length of the numbers list
    if length_of_number_list == 0:
        # checks if there are items in the list, if not, returns an empty list
        return []

    longest_sequence_modulo_list = [1] * length_of_number_list  # we create a list to store the longest sequence up to a point
    previous_position_index = [-1] * length_of_number_list  # we create another list in which we store the positions of the numbers
    # in the original list which added to the subsequence. This is useful for reconstructing the subsequence

    for i in range(1, length_of_number_list):
        for j in range(i):

            if modulo(number_list[j]) < modulo(number_list[i]) and longest_sequence_modulo_list[
                j] + 1 > longest_sequence_modulo_list[i]:
                # checks if the modulo of the first number is bigger than of the second,
                # if so it adds the number to the subsequence and stores the position of that number in the original list
                longest_sequence_modulo_list[i] = longest_sequence_modulo_list[j] + 1
                previous_position_index[i] = j

    max_len = max(longest_sequence_modulo_list)  # we look in the list for the longest subsequence
    max_index = longest_sequence_modulo_list.index(max_len)

    reconstructed_list = []
    # we reconstruct the subsequence
    while max_index != -1:
        reconstructed_list.append(number_list[max_index])
        max_index = previous_position_index[max_index]

    reconstructed_list.reverse()
    # we reverse the subsequence since it will be built in descending order
    return reconstructed_list


def modulo(param):
    # returns the modulo of the complex number
    return (param[0] ** 2 + param[1] ** 2) ** 0.5


def modulo_dictionary(param):
    # returns the modulo of the complex number
    return (param.get("real") ** 2 + param.get("imaginary") ** 2) ** 0.5


def longest_increasing_subsequence_modulo_dictionary(number_list):
    length_of_number_list = len(number_list)  # stores the length of the numbers list
    if length_of_number_list == 0:
        # checks if there are items in the list, if not, returns an empty list
        return []

    longest_sequence_modulo_list = [1] * length_of_number_list  # we create a list to store the longest sequence up to a point
    previous_position_index = [-1] * length_of_number_list  # we create another list in which we store the positions of the numbers
    # in the original list which added to the subsequence. This is useful for reconstructing the subsequence

    for i in range(1, length_of_number_list):
        for j in range(i):

            if modulo_dictionary(number_list[j]) < modulo_dictionary(number_list[i]) and longest_sequence_modulo_list[
                j] + 1 > longest_sequence_modulo_list[i]:
                # checks if the modulo of the first number is bigger than of the second,
                # if so it adds the number to the subsequence and stores the position of that number in the original list
                longest_sequence_modulo_list[i] = longest_sequence_modulo_list[j] + 1
                previous_position_index[i] = j

    max_len = max(longest_sequence_modulo_list)  # we look in the list for the longest subsequence
    max_index = longest_sequence_modulo_list.index(max_len)

    reconstructed_list = []
    # we reconstruct the subsequence
    while max_index != -1:
        reconstructed_list.append(number_list[max_index])
        max_index = previous_position_index[max_index]

    reconstructed_list.reverse()
    # we reverse the subsequence since it will be built in descending order
    return reconstructed_list


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def input_complex_number_list(number_list):
    try:
        real_part = int(input("Enter the real part of your number: "))
        imaginary_part = int(input("Enter the imaginary part of your number: "))
        complex_number = create_complex_number_list(real_part, imaginary_part)
        add_number_to_list(number_list, complex_number)
        print("Number added successfully!")
        print()
    except ValueError as ve:
        print(str(ve))
        return


def input_complex_number_dictionary(number_dictionary):
    try:
        real_part = int(input("Enter the real part of your number: "))
        imaginary_part = int(input("Enter the imaginary part of your number: "))
        number_dictionary.append({"real": real_part, "imaginary": imaginary_part})
        print("Number added successfully!")
        print()
    except ValueError as ve:
        print(str(ve))
        return


def display_list_of_complex_numbers(number_list):
    for lists in number_list:
        if get_imaginary_part(lists) != 0:
            print("z = " + str(get_real_part(lists)) + ' + ' + str(get_imaginary_part(lists)) + 'i')
        else:
            print("z = " + str(get_real_part(lists)))


def display_dictionary_of_complex_numbers(number_dictionary):
    for numbers in number_dictionary:
        real = numbers.get('real')
        imaginary = numbers.get('imaginary')
        print('z = ' + str(real) + ' + ' + str(imaginary) + 'i')


def print_menu_dictionary():
    print("1.Read a dictionary of complex numbers (in z = a + bi form) from the console.")
    print("2.Display the entire dictionary of numbers on the console.")
    print("3.Display on the console the longest subarray of distinct numbers.")
    print("4.Display on the console one of the longest increasing subsequences, when considering each number's modulus.")
    print("0.Exit")
    print()


def print_menu():
    print("1. List approach.")
    print("2. Dictionary approach.")
    print("0. Exit")
    print()


def print_menu_list():
    print("1.Read a list of complex numbers (in z = a + bi form) from the console.")
    print("2.Display the entire list of numbers on the console.")
    print("3.Display on the console the longest subarray of distinct numbers.")
    print("4.Display on the console one of the longest increasing subsequences, when considering each number's modulus.")
    print("0.Exit")
    print()


def start():
    number_list = []
    number_dictionary = []
    initial_complex_numbers_list(number_list)
    initial_complex_numbers_dictionary(number_dictionary)

    print_menu()
    choice = input("Choose an option = ")
    match choice:
        case "1":
            while True:
                print_menu_list()
                choice_list = input("Choose an option = ")
                match choice_list:

                    case "1":
                        input_complex_number_list(number_list)

                    case "2":

                        display_list_of_complex_numbers(number_list)

                    case "3":

                        print(longest_distinct_subarray(number_list))

                    case "4":

                        print(longest_increasing_subsequence_modulo(number_list))

                    case "0":
                        break

                    case default:
                        print("Please enter a valid option!")
        case "2":
            while True:
                print_menu_dictionary()
                choice_dictionary = input("Choose an option = ")
                match choice_dictionary:
                    case "1":
                        input_complex_number_dictionary(number_dictionary)

                    case "2":
                        display_dictionary_of_complex_numbers(number_dictionary)

                    case "3":
                        print(longest_distinct_subarray(number_dictionary))

                    case "4":
                        print(longest_increasing_subsequence_modulo_dictionary(number_dictionary))

                    case "0":
                        break

                    case default:
                        print("Please enter a valid option!")
        case "0":
            pass

        case default:
            print("Please enter a valid option!")


if __name__ == "__main__":
    print("Make magic happen")
    start()
    test_longest_distinct_subarray()
    test_create_complex_numbers()
    test_get_real_and_imaginary_parts()
    test_modulo()
    test_longest_subsequence()
