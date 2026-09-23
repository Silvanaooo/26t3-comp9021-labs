def f6_1(filename: str) -> None:
    """
    Reads a text file line by line and prints symbols repeated by count.
    Skips lines that only contain whitespace using `isspace()`.
    """
    with open(filename) as file:
        for line in file:
            # Skip lines that are just spaces or empty
            if not line.isspace():
                # Split into count and symbol
                count, symbol = line.split()
                if count:
                    print(int(count) * symbol)


def f6_2(filename: str) -> None:
    """
    Reads a text file line by line and prints symbols repeated by count.
    Cleans up lines first using `strip()`.
    """
    with open(filename) as file:
        for line in file:
            # Remove leading/trailing spaces and check if non-empty
            line = line.strip()
            if line:
                # Split into count and symbol
                count, symbol = line.split()
                if count:
                    print(int(count) * symbol)