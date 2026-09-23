def f5_1(filename: str) -> None:
    """
    Reads a file line by line using direct iteration over the file object.
    Processes each line with split().
    """
    with open(filename) as file:
        for line in file:
            # Split into name and count
            name, count = line.split(",")
            print(int(count) * 1000, "people named", name)


def f5_2(filename: str) -> None:
    """
    Reads the whole file content at once and then iterates with splitlines().
    Processes each line with split().
    """
    with open(filename) as file:
        for line in file.read().splitlines():
            # Split into name and count
            name, count = line.split(",")
            print(int(count) * 1000, "people named", name)