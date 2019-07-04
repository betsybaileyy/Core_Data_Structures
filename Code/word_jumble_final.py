
# getting the computer's default dictionary and
def get_file_lines(filename='/usr/share/dict/words'):
    """Return a set from the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    new_set = set(lines)
    return lines

# getting all the possible permutations of the current word
def all_perms(word):
'''
Taking each possible permutation of the word we are given
'''
   if len(word) <=1:
       return word
   else:
       final_words = []
       for perm in all_perms(word[1:]):
           for i in range(len(word)):
               curr_perm = perm[:i] + word[0:1] + perm[i:]
               if curr_perm not in final_words:
                   final_words.append(curr_perm)

       return final_words

def word_search(words, dictionary):
    '''
        Goes through words [list] and checks if its in the dictionary (set) of word_set
        O(n) -> len of words

        Return word_found -> list of words found in dict.
    '''
    word_found = []
    for word in words:
        if word in dictionary:
            word_found.append(word)

    return word_found

def solve_word_jumble(word_perms):
    final_words = []
    word_set = get_file_lines()
    for word in word_perms:
        all_perms = all_perms(word)
        word_found = word_search(all_perms, word_set)
        final_words.append(word_found)

    print('hello')
    return final_words

def main():
    # Word Jumble 1. Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his ___."
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    # circles1 = ['__O_O', 'OO_O_', '____O_', '___OO_']
    # final1 = ['OO', 'OOOOOO']
    print(solve_word_jumble(words1))
