def f6_1(L: list[list[int]], fields: list[int]) -> list[list[int]]:
    """
    Sorts a list of lists of integers based on specified fields priority.
    
    Uses Python's built-in sorted function with a custom key function that creates
    a tuple of values in the order specified by fields.
    
    :param L: A list of lists of integers. All inner lists have the same length n.
    :param fields: A list representing a permutation of {1, ..., n}, giving sort priority.
    :return: A new list sorted according to the multi-key priority in `fields`.
    """
    # Use sorted with a custom key function
    # - The lambda creates a tuple of values for each inner list
    # - For each position i in fields, we get the corresponding value from the inner list (x[i-1])
    # - The tuple is then used for comparison, checking elements in the order specified by fields
    return sorted(L, key=lambda x: tuple(x[i - 1] for i in fields))

def f6_2(L: list[list[int]], fields: list[int]) -> list[list[int]]:
    """
    Sort a list of equal-length integer rows by multiple columns (in priority order).
    We sort first by the column at fields[0], then break ties by fields[1], etc.

    :param L: A list of lists of integers. All inner lists have the same length n.
    :param fields: A list representing a permutation of {1, ..., n}, giving sort priority.
    :return: A new list sorted according to the multi-key priority in `fields`.
    """
    # Helper: build the tuple key for one row in the exact order given by `fields`.
    def make_key(row: list[int]) -> tuple[int]:
        key_parts = []
        for f in fields:
            # fields is 1-based; Python lists are 0-based.
            key_parts.append(row[f - 1])
        return tuple(key_parts)

    # Use the helper function as the key for sorted()
    return sorted(L, key=make_key)