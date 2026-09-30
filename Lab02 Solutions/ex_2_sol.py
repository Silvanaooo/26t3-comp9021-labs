def f2(text: str) -> str:
    """
    Normalize a text:
    - First word of each sentence is capitalized
    - All other words are lowercase
    - Extra spaces are removed
    :param text: (str) The input text to process
    :return: (str) The processed text with proper sentence capitalization
    """
    # Split the input text into a list of words
    words = text.split()

    for i in range(len(words)):
        # If this is the first word in the text OR
        # the previous word ends with a sentence-ending punctuation mark
        if i == 0 or words[i - 1][-1] in ".!?":
            # Capitalize the first letter of the word (title case)
            words[i] = words[i].title()
        else:
            # Otherwise, convert the word to lowercase
            words[i] = words[i].lower()

    # Rejoin the processed words with spaces and return the result
    return " ".join(words)