#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Best Case Run Time: 0(1) if at begining of string
    Worst Case: 0(n) if item is not at begining
    Space complexity: 0(n) because we are relaiant on the size of text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    index = find_index(text, pattern)
    if index is not None:
        return True
    else:
        return False


def find_index(text, pattern, offset=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Run time: 0(n) we are iterating through each index and checking it against the pattern
    Space complexity: 0(n) because we are relaiant on the size of text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    if(len(pattern) == 0):
        return offset

    for i in range(offset, len(text) - len(pattern) + 1):
        if(text[i] == pattern[0]):

            no_misses = True  #assumption that pattern matches
            for j in range(len(pattern)): # j is the index number in the pattern, not the text

                # checking if pattern matches incrementally
                if(pattern[j] != text[i + j]): # i is the index of the text, and j is index of pattern, so, added, they equal the correct index of the text snippet that we are looking for

                    no_misses = False # assumption is wrong
                    break

            if(no_misses): # if assumption is true
                return i

    return None



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Run time: 0(n) we are iterating through each index and checking it against the pattern
    Space complexity: 0(n) because we are relaiant on the size of text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    index = find_index(text, pattern)
    pattern_indexes = []

    if(len(pattern) == 0):
        return list(range(0,len(text)))

    while index is not None:
        offset = index + 1
        pattern_indexes.append(index)
        index = find_index(text, pattern, offset)

    return pattern_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
