def f1_1(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    
    Uses nested list comprehensions with join method to create the pattern.
    
    :param m: Number of parts to repeat.
    :param n: Number of underscores in each part.
    :return: A string with m groups of n underscores separated by '|',
        with groups separated by ' * '
        Returns an empty string if m or n is 0.
    """
    # Inner comprehension: Create n underscores joined by '|' for each row
    # Outer comprehension: Create m rows and join them with ' * '
    return ' * '.join('|'.join('_' for _ in range(n)) for _ in range(m))

def f1_2(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    String construction approach, using string multiplication and join() to build the result directly.
    :param m: Number of parts to repeat.
    :param n: Number of underscores in each part.
    :return: A string with m groups of n underscores separated by '|',
        with groups separated by ' * '
        Returns an empty string if m or n is 0.
    """
    if m == 0 or n == 0:
        return ''
    part = "_|" * (n - 1) + "_"
    return (" * ".join([part] * m) + "\n").strip()


def f1_3(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    
    Uses explicit for loops with join method to create the pattern.
    
    :param m: Number of parts to repeat.
    :param n: Number of underscores in each part.
    :return: A string with m groups of n underscores separated by '|',
        with groups separated by ' * '
        Returns an empty string if m or n is 0.
    """
    rows = []  # Initialize list to store all rows
    for _ in range(m):  # Iterate m times to create m rows
        elements = []  # Initialize list to store elements in current row
        for _ in range(n):  # Iterate n times to create n underscores
            elements.append('_')  # Add an underscore to the current row
        row = '|'.join(elements)  # Join all underscores with '|' separator
        rows.append(row)  # Add the completed row to our collection
    return ' * '.join(rows)  # Join all rows with ' * ' separator