#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
import colorama
from colorama import Fore

from src.functions import initial_complex_numbers_list, input_complex_number_list, insert_number_at_position, undo, \
    display_list_position_to_position, display_list_modulo, table_for_display_list, remove_number_at_position, \
    remove_numbers_from_position_to_position, replace_number, filter_real, filter_modulo
from src.ui import print_menu, print_menu_add_number, input_complex_number, input_position, pretty_print, \
    print_menu_modify_number, input_number_from_list, print_menu_display, sign_input, input_compare_number, \
    print_menu_filter, choice1_1, choice1_2, choice2_1, choice2_2, choice2_3, choice3_1, choice3_2, choice3_3, choice4_1, choice_undo, choice4_2
from src.tests import test_modulo, test_create_complex_number, test_get_real_part, test_get_imaginary_part, \
    test_check_if_in_list, test_is_comparison_sign, test_complex_numbers_to_string


def main():
    history = []
    colorama.init(autoreset=True)
    number_list = []
    initial_complex_numbers_list(number_list)
    while True:

        print_menu()
        choice = input("Choose an option = ")
        print()
        match choice:
            case "1":
                while True:
                    print_menu_add_number()
                    choice1 = input("Choose an option = ")
                    print()
                    match choice1:
                        case "1":
                            choice1_1(number_list, history)
                        case "2":
                            choice1_2(number_list, history)
                        case "3":
                            number_list = choice_undo(history)
                        case "0":
                            break
                        case default:
                            print(Fore.RED + "ERROR!Please enter a valid option!")
            case "2":
                while True:
                    print_menu_modify_number()
                    choice2 = input("Choose an option = ")
                    print()
                    match choice2:
                        case "1":

                            choice2_1(number_list, history)

                        case "2":

                            choice2_2(number_list, history)

                        case "3":
                            choice2_3(number_list, history)
                        case "4":
                            number_list = choice_undo(history)
                        case "0":
                            break
                        case default:
                            print(Fore.RED + "ERROR!Please enter a valid option!")

            case "3":
                while True:
                    print_menu_display()
                    choice3 = input("Choose an option = ")
                    print()
                    match choice3:
                        case "1":
                            choice3_1(number_list)
                        case "2":
                            choice3_2(number_list)
                        case "3":
                            choice3_3(number_list)
                        case "0":
                            break
                        case default:
                            print(Fore.RED + "ERROR!Please enter a valid option!")

            case "4":
                while True:
                    print_menu_filter()
                    choice4 = input("Choose an option = ")
                    print()
                    match choice4:
                        case "1":
                            choice4_1(number_list, history)
                        case "2":
                            choice4_2(number_list, history)
                        case "3":
                            number_list = choice_undo(history)
                        case "0":
                            break
                        case default:
                            print(Fore.RED + "ERROR!Please enter a valid option!")

            case "0":
                break

            case default:
                print(Fore.RED + "ERROR!Please enter a valid option!")


if __name__ == "__main__":
    main()
    test_modulo()
    test_create_complex_number()
    test_get_real_part()
    test_get_imaginary_part()
    test_check_if_in_list()
    test_is_comparison_sign()
    test_complex_numbers_to_string()
