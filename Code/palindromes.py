#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    clean_text = re.sub('[^A-Za-z0-9]+', '', text).lower()
    return is_palindrome_iterative(clean_text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively here
    left_index = 0
    right_index = len(text) -1

    while left_index <= right_index:
        if text[left_index] == text[right_index]: #check that both indexes match
            #continue the loop by moving to next index
            left_index += 1
            right_index -= 1
        else: #if not, cancel the function bc we immiedetly know it is not a palindrome
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    if right == None:
        left = 0
        right = len(text) - 1
    if left >= right:
        return True
    if text[right] == text[left]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
