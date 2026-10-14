
"""
Prompts the user for a sequence of uppercase letters and finds the
shortest dictionary words that contain all those letters (in order).

The program:
  1. Keeps only uppercase letters from user input (warns if others exist)
  2. Reads words from 'dictionary.txt' (one uppercase word per line)
  3. Finds all dictionary words that embed the given letters in order
  4. Outputs:
     - A warning if no matching word exists
     - A message if the input itself is a dictionary word
     - A list of all shortest matching words otherwise

Example:
    Input: priceECIRPprice
    Output:
        I only keep the uppercase letters, so work with 'ECIRP'.
        The shortest words in the dictionary that embed 'ECIRP' are:
            ELECTROCARDIOGRAPH
"""

# Step 1: Handle user input
letters = input('Enter uppercase letters: ')

# Keep only uppercase letters; warn the user if anything was removed
if not all(c.isupper() for c in letters):
    letters = ''.join(c for c in letters if c.isupper())
    print(f"I only keep the uppercase letters, so work with '{letters}'.")

# Step 2: Process the dictionary
with open('dictionary.txt') as dictionary:
    min_length = float('inf')  # Tracks shortest matching word length
    words = []  # Stores all shortest matching words

    for word in dictionary:
        word = word.rstrip()  # Remove trailing newline

        # Skip if current word is longer than already found minimal + 1
        if len(word) > min_length + 1:
            continue

        # Step 3: Check if 'letters' is a subsequence of 'word'
        index = 0
        for e in letters:
            index = word.find(e, index)
            if index == -1:
                break
        else:
            # If we didn't break, 'letters' is a subsequence of 'word'
            if len(word) < min_length:
                # Found a shorter word → reset list
                min_length = len(word)
                words = [word]
            elif len(word) == min_length:
                # Found another word of the same minimal length
                words.append(word)

# Step 4: Output results
if not words:
    print('No word in the dictionary embeds', letters, end='.\n')

elif len(words) == 1 and words[0] == letters:
    print(letters, 'is a word in the dictionary.')

else:
    print(f"The shortest words in the dictionary that embed '{letters}' are:")
    for word in words:
        print('   ', word)



# Option 2 for Step 2
def find_minimal_extensions(word: str) -> list[str]:
    """
    Finds all shortest dictionary words that embed a given uppercase pattern
    as a subsequence.

    A word W is said to embed the sequence 'word' if all letters of 'word'
    appear in W in the same order (but not necessarily consecutively).

    Example:
        If word = 'ECIRP', and dictionary.txt contains 'ELECTROCARDIOGRAPH',
        then that word is a valid embedding.

    This function:
        1. Reads words from 'dictionary.txt' (one per line).
        2. Checks each word to see if it contains 'word' as a subsequence.
        3. Collects all matches and keeps only those with minimal length.

    :param word: A string of uppercase letters (pattern to embed)
    :return: A list of shortest dictionary words that embed the given pattern
    """
    result = []

    def is_subsequence(target, text):
        """
        Check if target is a subsequence of text using two pointers.

        Args:
            target (str): The string to find as a subsequence.
            text (str): The string to search within.

        Returns:
            bool: True if target is a subsequence of text, False otherwise.
        """
        i, j = 0, 0  # Initialize two pointers

        # Move through both strings with two pointers
        while i < len(target) and j < len(text):
            if target[i] == text[j]:
                i += 1  # Move target pointer only when characters match
            j += 1  # Always move text pointer forward

        # If we've matched all characters in target, it's a subsequence
        return i == len(target)

    # Open the dictionary file (each line is one uppercase word)
    with open("dictionary.txt") as file:
        for line in file:
            # Skip lines that contain only whitespace
            if not line.isspace():
                line = line.strip()  # remove trailing newline or spaces
                if is_subsequence(word, line):
                    result.append(line)

    new_result = []

    if result:
        # Step 1: find the minimum length among all matched words
        min_len = min([len(letter) for letter in result])

        # Step 2: keep only words of minimal length
        for letter in result:
            if len(letter) == min_len:
                new_result.append(letter)

        # Return all shortest matches
        return new_result
    else:
        # No matches found in dictionary
        return []



def find_minimal_extensions_2(word: str) -> None:
    """
    Finds all shortest dictionary words that embed a given uppercase pattern
    as a subsequence.

    A word W is said to embed the sequence 'word' if all letters of 'word'
    appear in W in the same order (but not necessarily consecutively).

    Example:
        If word = 'ECIRP', and dictionary.txt contains 'ELECTROCARDIOGRAPH',
        then that word is a valid embedding.

    This function:
        1. Reads words from 'dictionary.txt' (one per line).
        2. Checks each word to see if it contains 'word' as a subsequence.
        3. Collects all matches and keeps only those with minimal length.

    :param word: A string of uppercase letters (pattern to embed)
    :return: A list of shortest dictionary words that embed the given pattern
    """
    result = []
    min_length = float('inf')
    # Open the dictionary file (each line is one uppercase word)
    with open("dictionary.txt") as file:
        for line in file:
            if not line.isspace():
                line = line.strip()

                # Pruning:
                # if this word is already longer than the shortest valid word found,
                # there is no need to check it
                if len(line) > min_length:
                    continue

                k = 0  # pointer for the pattern string 'word'

                for letter in range(len(line)):
                    if k < len(word) and line[letter] == word[k]:
                        k += 1

                    if k == len(word):
                        if len(line) < min_length:
                            min_length = len(line)
                            result = [line]
                        elif len(line) == min_length:
                            result.append(line)
                        break

    if not result:
        print('No word in the dictionary embeds', word, end='.\n')
    elif len(result) == 1 and result[0] == word:
        print(word, 'is a word in the dictionary.')
    else:
        print(f"The shortest words in the dictionary that embed '{word}' are:")
        for w in result:
            print('   ', w)