# Determine the longest common subsequence of two given sequences. Subsequence elements are not required to occupy consecutive positions.
# For example, if X = "MNPNQMN" and Y = "NQPMNM", the longest common subsequence has length 4, and can be one of "NQMN", "NPMN" or "NPNM".
# Determine and display both the length of the longest common subsequence as well as at least one such subsequence.

# M N P N Q M N
# N Q P M N M
from colorama import Fore
import colorama

def test_sequence_length():
    assert sequence_length("MNPOQ", "ABCD") == (5, 4)
    assert sequence_length("", "") == (0,0)
    assert sequence_length("Ana are mere", "Andrei are pere") == (12, 15)

def test_longest_common_subsequence_value():
    assert longest_common_subsequence_value("MNOP", "ABC") == 0
    assert longest_common_subsequence_value("1234", "123") == 3
    assert longest_common_subsequence_value("a 2 3 4", "b 5 6 7") == 0
    assert longest_common_subsequence_value("ana are mere", "ana are pere") == 9
    assert longest_common_subsequence_value("a", "b") == 0

def test_longest_common_subsequence_items():
    assert longest_common_subsequence_items("ABCD", "ABCD") == "ABCD"
    assert longest_common_subsequence_items("1234", "3564") == "34"
    assert longest_common_subsequence_items("caini", "pisici") == "ii"

def test_list_to_string():
    assert list_to_string([1, 2, 3]) == "123"
    assert list_to_string(['a', 'b', 'c']) == "abc"
    assert list_to_string(['b', '2', 'e', 'r']) == "b2er"


def sequence_length(sequence1, sequence2):
    lenSeq1, lenSeq2 = len(sequence1), len(sequence2)
    return lenSeq1, lenSeq2

def create_matrix_with_sequence_lengths(sequence1, sequence2, lenSeq1, lenSeq2):
    sequence_matrix = [[0] * (lenSeq2 + 1) for _ in range(lenSeq1 + 1)]
    for index1 in range(1, lenSeq1 + 1):
        for index2 in range(1, lenSeq2 + 1):
            if sequence1[index1 - 1] == sequence2[index2 - 1] and sequence1[index1 - 1] != " ":
                sequence_matrix[index1][index2] = sequence_matrix[index1 - 1][index2 - 1] + 1
            else:
                sequence_matrix[index1][index2] = max(sequence_matrix[index1 - 1][index2], sequence_matrix[index1][index2 - 1])
    return sequence_matrix

def longest_common_subsequence_value(sequence1, sequence2):
    lenSeq1, lenSeq2 = sequence_length(sequence1, sequence2)
    sequence_matrix = create_matrix_with_sequence_lengths(sequence1, sequence2, lenSeq1, lenSeq2)
    longest_common_subsequence_length = sequence_matrix[lenSeq1][lenSeq2]
    return longest_common_subsequence_length

def list_to_string(list):
    lcs_string = ""
    for i in range(len(list)):
        lcs_string += str(list[i])
    return lcs_string


def longest_common_subsequence_items(sequence1, sequence2):
    lenSeq1, lenSeq2 = sequence_length(sequence1, sequence2)
    sequence_matrix = create_matrix_with_sequence_lengths(sequence1, sequence2, lenSeq1, lenSeq2)

    index1, index2 = lenSeq1, lenSeq2
    longest_common_subsequence = []
    while index1 > 0 and index2 > 0:
        if sequence1[index1 - 1] == sequence2[index2 - 1] and sequence1[index1 - 1] != " ":
            longest_common_subsequence.append(sequence1[index1  - 1])
            index1 -= 1
            index2 -= 1
        elif sequence_matrix[index1 - 1][index2] > sequence_matrix[index1][index2 - 1]:
            index1 -= 1
        else:
            index2 -= 1
    longest_common_subsequence.reverse()
    longest_common_subsequence = list_to_string(longest_common_subsequence)
    return longest_common_subsequence


def print_result(length, items):
    if length == 0:
        print(Fore.LIGHTGREEN_EX + "There is no common subsequence.")
    else:
        print(Fore.LIGHTMAGENTA_EX + "Length of Longest Common Subsequence:", length)
        print(Fore.LIGHTMAGENTA_EX + "One of the Longest Common Subsequences is:", items)

def main():
        colorama.init(autoreset=True)
        Sequence1 = input("Enter a sequence:")
        while Sequence1 == "" or Sequence1 == " ":
            print(Fore.LIGHTRED_EX + "ERROR!Please enter a non-null sequence!")
            Sequence1 = input("Enter a sequence:")
        Sequence2 = input("Enter another sequence:")
        while Sequence2 == "" or Sequence2 == " ":
            print(Fore.LIGHTRED_EX + "ERROR!Please enter a non-null sequence!")
            Sequence2 = input("Enter another sequence:")

        length = longest_common_subsequence_value(Sequence1, Sequence2)
        items = longest_common_subsequence_items(Sequence1, Sequence2)

        print_result(length, items)


if __name__ == '__main__':
    main()
    test_sequence_length()
    test_longest_common_subsequence_value()
    test_longest_common_subsequence_items()
    test_list_to_string()