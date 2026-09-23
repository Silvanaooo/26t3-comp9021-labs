def f1(m: int, n: int) -> str:
    """
    Creates a pattern of m segments,
    each containing a pair of vertical bars with n underscores between them.
    :param m: (int) Number of segments to repeat.
    :param n: (int) Number of underscores inside each segment.
    :return:
        str: The resulting pattern string formed by repeating the segment `m` times.
    """
    segment = "|" + "_" * n + "|" # Build one segment: | + n underscores + |
    return segment * m # Repeat the segment m times to form the full pattern


def f1_2(m: int, n: int) -> str:
    """
    Creates a pattern of m segments, each containing a pair of vertical bars with n underscores between them.
    Implements the solution using a for loop and string concatenation.
    """
    result = ""
    for _ in range(m):
        result += "|" + "_" * n + "|"
    return result
