# Assume that the argument L is a list of integers.
#
# Lists are, if possible, broken down into sublists
# all the same length, that length being maximal,
# those sublists themselves being, if possible,
# broken down into sublists all the same length,
# that length being maximal...
#
# The original list is preserved.

from math import sqrt
def f4(L: list[int]):
    """
    Recursively breaks down a list into nested sublists of maximal equal length.

    This implementation searches for the largest divisor of the list length
    that is less than or equal to the square root of the length. If found,
    it divides the list into sublists of that length and recursively applies
    the same process to each sublist.

    Args:
        L: A list of integers

    Returns:
        A new list that may contain nested sublists, or a copy of the original list
        if no further breakdown is possible

    Example:
        f4_1([1, 2, 3, 4]) returns [[1, 2], [3, 4]]
        f4_1([1, 2, 3, 4, 5, 6]) returns [[1, 2, 3], [4, 5, 6]]
        f4_1([1, 2, 3, 4, 5, 6, 7, 8, 9]) returns [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    # Handle empty list or single element list
    if len(L) <= 1:
        return list(L)

    # Search for the largest divisor <= sqrt(len(L))
    for n in range(2, round(sqrt(len(L))) + 1):
        if len(L) % n == 0:
            # Calculate the width of each sublist
            w = len(L) // n
            # Create n sublists of width w and recursively process each
            return [f4(L[i : i + w]) for i in range(0, len(L), w)]

    # If no suitable divisor is found, return a copy of the list
    return list(L)
