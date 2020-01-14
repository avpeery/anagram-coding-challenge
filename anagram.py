"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""

import os, sys

all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]



def find_most_anagrams_from_wordlist(wordlist):

    """Given list of words, return the word with the most anagrams."""

    anagram_dict = make_anagram_dict(wordlist)

    longest_anagrams = 0
    most_anagrams = None

    for word in wordlist:
        sorted_word = "".join(sorted(word))
        number_anagrams = len(anagram_dict[sorted_word])
        if number_anagrams > longest_anagrams:
            longest_anagrams = number_anagrams
            most_anagrams = word

    return most_anagrams

def make_anagram_dict(words):

    new_dict = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        new_dict.setdefault(sorted_word, []).append(word)
            
    return new_dict

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
