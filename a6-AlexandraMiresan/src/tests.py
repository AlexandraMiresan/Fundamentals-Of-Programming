from src.functions import create_complex_number, get_real_part, get_imaginary_part, check_if_in_list, \
    is_comparison_sign, complex_numbers_to_string, modulo


def test_create_complex_number():
    assert create_complex_number(2, 3) == [2, 3]
    assert create_complex_number(65, 0) == [65, 0]
    assert create_complex_number(0, 10) == [0, 10]


def test_get_real_part():
    assert get_real_part([2, 3]) == 2
    assert get_real_part([0, 8]) == 0
    assert get_real_part([1, 7]) == 1


def test_get_imaginary_part():
    assert get_imaginary_part([2, 3]) == 3
    assert get_imaginary_part([0, 8]) == 8
    assert get_imaginary_part([1, 7]) == 7

def test_check_if_in_list():
    assert check_if_in_list([2, 3, 4, 5, 6], 5) == True
    assert check_if_in_list([2, 9, 6, 10], 7) == False
    assert check_if_in_list([1, 2, 3, 4, 5, 6], 5) == True

def test_is_comparison_sign():
    assert is_comparison_sign('>') == True
    assert is_comparison_sign('<') == True
    assert is_comparison_sign('=') == True
    assert is_comparison_sign('>=') == True
    assert is_comparison_sign('<=') == True
    assert is_comparison_sign('a') == False

def test_complex_numbers_to_string():
    assert complex_numbers_to_string([2, 5]) == "z = 2+5i"
    assert complex_numbers_to_string([23, 12]) == "z = 23+12i"
    assert complex_numbers_to_string([2, 3]) == "z = 2+3i"
    assert complex_numbers_to_string([0, 3]) == "z = 3i"
    assert complex_numbers_to_string([2, 0]) == "z = 2"

def test_modulo():
    assert modulo([4, 3]) == 5
    assert modulo([6, 8]) == 10

