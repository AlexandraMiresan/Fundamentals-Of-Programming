# Determine the longest common subsequence of two given sequences. Subsequence elements are not required to occupy consecutive positions.
# For example, if X = "MNPNQMN" and Y = "NQPMNM", the longest common subsequence has length 4, and can be one of "NQMN", "NPMN" or "NPNM".
# Determine and display both the length of the longest common subsequence as well as at least one such subsequence.
import colorama
from colorama import Fore
from dynamic_programming import print_result

def test_longest_common_subsequence():
    assert longest_common_subsequence("abcd", "abcd") == "abcd"
    assert longest_common_subsequence("12345", "134885") == "1345"
    assert longest_common_subsequence("ana are mere", "ana are pere") == "anaareere"
    assert longest_common_subsequence("a 2 3 4", "bcd") == ""

def longest_common_subsequence(sequence1, sequence2):
    if not sequence1 or not sequence2:
        return ""

    if sequence1[0] == sequence2[0] and sequence1[0] != " ":
        return sequence1[0] + longest_common_subsequence(sequence1[1:], sequence2[1:])
    else:
        longest_common_subsequence1 = longest_common_subsequence(sequence1[1:], sequence2)
        longest_common_subsequence2 = longest_common_subsequence(sequence1, sequence2[1:])
        if len(longest_common_subsequence1) > len(longest_common_subsequence2):
            return longest_common_subsequence1
        else:
            return longest_common_subsequence2

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

    item = longest_common_subsequence(Sequence1, Sequence2)
    length = len(item)
    print_result(length, item)

if __name__ == '__main__':
    main()
    test_longest_common_subsequence()