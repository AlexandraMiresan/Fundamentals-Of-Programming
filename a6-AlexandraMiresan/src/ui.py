#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import colorama
from colorama import Fore
from functions import *
from functions import create_complex_number


def print_menu():
    print("1. Add a number.")
    print("2. Modify numbers.")
    print("3. Display numbers having different properties.")
    print("4. Filter the list by different criteria.")
    print("0. Exit.")
    print()


def print_menu_add_number():
    print("1. Add a number.")
    print("2. Insert number at a specific position.")
    print("3. Undo.")
    print("0. Back.")
    print()


def print_menu_modify_number():
    print("1. Remove a number at a specific position.")
    print("2. Remove the numbers from a position to another.")
    print("3. Replace all occurrences of a number.")
    print("4. Undo.")
    print("0. Back.")
    print()


def print_menu_display():
    print("1. Display all the numbers.")
    print("2. Display the real numbers between two positions.")
    print("3. Display all numbers with modulo [ < | = | > ] to a certain value.")
    print("0. Back.")
    print()


def print_menu_filter():
    print("1. Filter the list by real numbers.")
    print("2. Filter the list by modulo [ < | = | > ] to a certain value.")
    print("3. Undo.")
    print("0. Back.")
    print()


def input_complex_number():
    colorama.init(autoreset=True)
    try:
        real_part = int(input(Fore.MAGENTA + "Real part = "))
        imaginary_part = int(input(Fore.MAGENTA + "Imaginary part = "))
        complex_number = create_complex_number(real_part, imaginary_part)
        return complex_number
    except ValueError as ve:
        print(Fore.RED + "ERROR!" + str(ve))
        print(Fore.RED + "Please enter an integer")


def input_position(number_list):
    colorama.init(autoreset=True)
    try:
        position = int(input(Fore.MAGENTA + "Position = "))
        while position > len(number_list):
            print(Fore.YELLOW + "Position is out of bounds. Please enter another position.")
            position = int(input(Fore.MAGENTA + "Position = "))
        return position
    except ValueError as ve:
        print(Fore.RED + "ERROR!" + str(ve))
        print(Fore.YELLOW + "Please enter an integer")


def input_compare_number():
    colorama.init(autoreset=True)
    try:
        compare_number = int(input("Please enter a positive number: "))
        return compare_number
    except ValueError as ve:
        print(Fore.RED + "ERROR!" + str(ve))
        print(Fore.YELLOW + "Please enter a positive number:")


def sign_input():
    colorama.init(autoreset=True)
    sign = input("Please enter a comparison sign: ")
    while not is_comparison_sign(sign):
        sign = input(Fore.YELLOW + "Please enter a valid comparison sign:")
    return sign


def input_number_from_list(number_list):
    complex_number = input_complex_number()
    while not check_if_in_list(number_list, complex_number):
        print(Fore.YELLOW + "The number is not in the list. Please enter another number.")
        complex_number = input_complex_number()
    return complex_number


def choice1_1(number_list, history):
    complex_number = input_complex_number()
    print(input_complex_number_list(number_list, complex_number, history))
    print()


def choice1_2(number_list, history):
    complex_number = input_complex_number()
    position = input_position(number_list)
    print(insert_number_at_position(number_list, position, complex_number, history))
    print()


def choice2_1(number_list, history):
    print("Please enter the position of the number you want to remove. ")
    position = input_position(number_list)
    print(remove_number_at_position(number_list, position, history))
    print()


def choice2_2(number_list, history):
    print("Please enter the starting position.")
    start_position = input_position(number_list)
    print("Please enter the ending position.")
    end_position = input_position(number_list)
    while start_position > end_position:
        print("The interval is invalid.")
        print()
        print("Please enter the starting position.")
        start_position = input_position(number_list)
        print("Please enter the ending position.")
        end_position = input_position(number_list)
    print(remove_numbers_from_position_to_position(number_list, start_position, end_position,
                                                   history))
    print()


def choice2_3(number_list, history):
    print("Please enter the number you want to replace:")
    initial_complex_number = input_number_from_list(number_list)
    print("Please enter the new number:")
    replace_complex_number = input_complex_number()
    print(replace_number(number_list, history, initial_complex_number, replace_complex_number))
    print()


def choice3_1(number_list):
    print(table_for_display_list(number_list).draw())
    print()


def choice3_2(number_list):
    print("Please enter the starting position.")
    start_position = input_position(number_list)
    print("Please enter the ending position.")
    end_position = input_position(number_list)
    while start_position > end_position:
        print("The interval is invalid.")
        print()
        print("Please enter the starting position.")
        start_position = input_position(number_list)
        print("Please enter the ending position.")
        end_position = input_position(number_list)
    print(display_list_position_to_position(number_list, start_position, end_position).draw())
    print()


def choice3_3(number_list):
    sign = sign_input()
    compare_number = input_compare_number()
    print(display_list_modulo(number_list, sign, compare_number).draw())
    print()


def choice4_1(number_list, history):
    filter_real(number_list, history)
    pretty_print(number_list)
    print()


def choice4_2(number_list, history):
    sign = sign_input()
    compare_number = input_compare_number()
    filter_modulo(number_list, sign, compare_number, history)
    pretty_print(number_list)
    print()


def choice_undo(history):
    try:
        number_list = undo(history)
        print("The last operation was undone.")
        return number_list
    except ValueError as ve:
        print("Undo not available.")
        print()


"""PRETTY PRINT"""


def pretty_print(number_list):
    for number in number_list:
        if get_imaginary_part(number) != 0:
            print("z = " + str(get_real_part(number)) + '+' + str(get_imaginary_part(number)) + "i")
        elif get_real_part(number) == 0:
            print("z = " + str(get_imaginary_part(number)) + "i")
        else:
            print("z = " + str(get_real_part(number)))
