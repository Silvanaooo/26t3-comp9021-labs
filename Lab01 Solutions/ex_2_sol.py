def f2_1(n: int) -> str:
    """
    Pattern with n lines, each line has n digits of n.
    Uses string multiplication + concatenation in one expression.
    """
    # Multiply string and add "\n", then repeat n times
    return (str(n) * n + "\n") * n


def f2_2(n: int) -> str:
    """
    Pattern with n lines, each line has n digits of n.
    Uses a loop with string concatenation.
    """
    result = ""
    # Build result line by line
    for _ in range(n):
        result += str(n) * n + "\n"
    return result


def f2_3(n: int) -> str:
    """
    Pattern with n lines, each line has n digits of n.
    Uses list comprehension + join to combine rows.
    """
    if n == 0:
        return ""

    # Create a list of rows first
    rows = [str(n) * n for _ in range(n)]
    # Join list into one string with newline separators
    return "\n".join(rows) + "\n"