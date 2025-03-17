#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import pdoc
import texttable
from texttable import *
import random

# TODO study pdoc

""""CREATE/EDIT COMPLEX NUMBER"""

def complex_numbers_to_string(complex_number):
    """
    takes a given complex number and returns a string consisting of that number
    :param complex_number: list consisting of real and imaginary part
    :return: "z = real_part +/- imaginary_part * i"
    """
    res = "z = " + str(get_real_part(complex_number))
    if get_imaginary_part(complex_number) != 0:
        if get_real_part(complex_number) == 0:
            res = "z = " + str(get_imaginary_part(complex_number)) + "i"
        elif get_imaginary_part(complex_number) > 0:
            res += "+" + str(get_imaginary_part(complex_number)) + "i"
        else:
            res += str(get_imaginary_part(complex_number)) + "i"
    elif get_imaginary_part(complex_number) == 0:
        res = "z = " + str(get_real_part(complex_number))
    return res

def create_complex_number(real_part: int, imaginary_part: int):
    """
    creates a complex number from a given real part and imaginary part
    :param real_part: integer
    :param imaginary_part: integer 
    :return: returns a list consisting of the real and imaginary part
    """
    return [real_part, imaginary_part]


def get_real_part(complex_number):
    return complex_number[0]


def get_imaginary_part(complex_number):
    return complex_number[1]


def initial_complex_numbers_list(number_list):
    """
    appends to a given list 10 randomly generated complex numbers, the complex numbers are
    represented as a list of two elements, the real part and the imaginary part.
    :param number_list: list
    :return:
    """
    for i in range(1, 11):
        real_part = random.randint(-100, 100)
        imaginary_part = random.randint(-100, 100)
        complex_number = create_complex_number(real_part, imaginary_part)
        add_number(complex_number, number_list)


def input_complex_number_list(number_list, complex_number, history):
    """
    appends to a given list, a given complex number and appends to another list (history) the list
    before adding the new complex number
    :param number_list: list to which we append the number
    :param complex_number: a list consisting of the real and imaginary part
    :param history: list
    :return:
    """
    history.append(number_list.copy())
    add_number(complex_number, number_list)
    return "The number was added successfully."


def check_if_in_list(number_list, complex_number):
    """
    checks if a given number is in the list
    :param number_list: list
    :param complex_number: list consisting of real and imaginary part
    :return: True if the number is in the list, False otherwise
    """
    for i in range(len(number_list)):
        if number_list[i] == complex_number:
            return True

    return False


def is_comparison_sign(sign):
    """
    checks if the value given to the function is a comparison sign
    :param sign: str
    :return: True if the value given to the function is a comparison sign, False otherwise
    """
    if sign == '>':
        return True
    elif sign == '<':
        return True
    elif sign == '=':
        return True
    elif sign == '>=':
        return True
    elif sign == '<=':
        return True

    return False


"""ADD A NUMBER"""


def add_number(complex_number, number_list):
    """
    appends to a given list, a given complex number
    :param complex_number: a list consisting of real and imaginary part
    :param number_list: list
    :return:
    """
    number_list.append(complex_number)



def insert_number_at_position(number_list, position: int, complex_number, history):
    """
    inserts at a given position in the list (number_list) a given complex number
    and appends to another list (history) the list before adding the new complex number
    :param number_list: list
    :param position: integer
    :param complex_number: a list consisting of real and imaginary part
    :param history: list
    :return: a message so that the user knows the operation was successful
    """
    history.append(number_list.copy())
    number_list.insert(position, complex_number)
    return "The number was inserted successfully."


"""MODIFY NUMBERS"""


def remove_number_at_position(number_list, position:int, history):
    """
    removes from a given position in the list (number_list) the complex number on that position
    and appends to another list (history) the list before removing the complex number
    :param number_list: list
    :param position: integer
    :param history: list
    :return:a message so that the user knows the operation was successful
    """
    history.append(number_list.copy())
    number_list.pop(position - 1)
    return "The number was removed successfully."


def remove_numbers_from_position_to_position(number_list, start_position, end_position, history):
    """
    removes from a given position in the list (number_list) to another given position, all the numbers on the position in between
    and appends to another list (history) the list before removing the complex numbers
    :param number_list: list
    :param start_position: integer
    :param end_position: integer
    :param history: list
    :return:a message so that the user knows the operation was successful
    """
    history.append(number_list.copy())
    for i in range(end_position - 1, start_position - 2, -1):
        number_list.pop(i)
    return "The numbers were removed successfully."


def replace_number(number_list, history, initial_complex_number, replace_complex_number):
    """
    replaces all the appearances of a given complex number with another given complex number
    and appends to another list (history) the list before replacing the complex numbers
    :param number_list: list
    :param history: list
    :param initial_complex_number: list consisting of real and imaginary part
    :param replace_complex_number: list consisting of real and imaginary part
    :return:
    """
    history.append(number_list.copy())
    for i in range(0, len(number_list)):
        if get_real_part(number_list[i]) == get_real_part(initial_complex_number) and get_imaginary_part(
                number_list[i]) == get_imaginary_part(initial_complex_number):
            number_list[i] = replace_complex_number
    return "The number was replaced successfully."


"""DISPLAY NUMBERS HAVING DIFFERENT PROPERTIES"""


def create_table():
    """
    creates a table
    :return: table
    """
    table = Texttable()
    table.add_row(['Complex Numbers'])
    return table





def table_for_display_list(number_list):
    """
    creates the table for displaying the whole list of complex numbers
    :param number_list: list
    :return: table
    """
    table = create_table()
    for term in range(len(number_list)):
        table.add_row([complex_numbers_to_string(number_list[term])])
    return table


def display_list_position_to_position(number_list, start_position, end_position):
    """
    creates the table for displaying the real numbers in the list in a given interval of positions
    :param number_list: list
    :param start_position: integer
    :param end_position: integer
    :return: table
    """
    table = create_table()
    for term in range(start_position - 1, end_position):
        if get_imaginary_part(number_list[term]) == 0:
            table.add_row([complex_numbers_to_string(number_list[term])])
    return table


def modulo(complex_number):
    """
    |a + b * i| = sqrt(a^2 + b^2)
    :param complex_number: list consisting of real and imaginary part
    :return: the modulo of the complex number
    """

    return (get_real_part(complex_number) ** 2 + get_imaginary_part(complex_number) ** 2) ** 0.5


def display_list_modulo(number_list, sign, compare_number):
    """
    creates the table for displaying the numbers whose modulo respect certain criteria
    :param number_list: list
    :param sign: string
    :param compare_number: a complex number represented as a list consisting of real and imaginary part
    :return: table
    """
    table = create_table()
    sign = sign.strip()
    for index in range(len(number_list)):
        if sign == '<':
            if modulo(number_list[index]) < compare_number:
                table.add_row([complex_numbers_to_string(number_list[index])])
        elif sign == '>':
            if modulo(number_list[index]) > compare_number:
                table.add_row([complex_numbers_to_string(number_list[index])])
        elif sign == '=':
            if modulo(number_list[index]) == compare_number:
                table.add_row([complex_numbers_to_string(number_list[index])])
        elif sign == '<=':
            if modulo(number_list[index]) <= compare_number:
                table.add_row([complex_numbers_to_string(number_list[index])])
        elif sign == '>=':
            if modulo(number_list[index]) >= compare_number:
                table.add_row([complex_numbers_to_string(number_list[index])])
    return table


"""FILTER THE LIST"""


def filter_real(number_list, history):
    """
    removes from the list all the numbers that are not real numbers
    :param number_list: list
    :return:
    """
    history.append(number_list.copy())
    for index in range(len(number_list) - 1, -1, -1):
        if get_imaginary_part(number_list[index]) != 0:
            number_list.pop(index)


def filter_modulo(number_list, sign, compare_number, history):
    """
    removes from the list all the numbers whose modulo does not respect the given criteria and saves the list in another list(history) before the modifications
    :param history: list
    :param number_list: list
    :param sign: string
    :param compare_number: a complex number represented as a list consisting of real and imaginary part
    :return:
    """
    history.append(number_list.copy())
    sign = sign.strip()
    for index in range(len(number_list) - 1, -1, -1):
        if sign == '<':
            if modulo(number_list[index]) < compare_number:
                number_list.pop(index)
        elif sign == '>':
            if modulo(number_list[index]) > compare_number:
                number_list.pop(index)
        elif sign == '=':
            if modulo(number_list[index]) == compare_number:
                number_list.pop(index)
        elif sign == '<=':
            if modulo(number_list[index]) <= compare_number:
                number_list.pop(index)
        elif sign == '>=':
            if modulo(number_list[index]) >= compare_number:
                number_list.pop(index)


"""UNDO"""


def undo(history):
    """
    reverts the last operation in the list
    :param history: list consisting of all the instances of the list throughout the code
    :return: the list before the last operation
    """
    if len(history) == 0:
        raise ValueError
    last_value = history.pop()
    return last_value
