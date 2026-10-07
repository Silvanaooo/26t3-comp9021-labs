def f3_1(n):
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    
    This function interprets the string representation of n as a number in different bases,
    and displays what those values would be in decimal (base 10).
    
    :param n: int in all possible bases
    :return: The result is printed out rather than returned.
    """
    # Convert the number to a string to analyze its digits
    n_str = str(n)
    
    # Find the minimum base required:
    # - The base must be at least 2 (binary)
    # - The base must be greater than the largest digit in the number
    # Using set comprehension to get all unique digits as integers
    max_digit = max(int(digit) for digit in n_str)
    min_base = max(2, max_digit + 1)
    
    # Iterate through all valid bases from min_base to base 10
    for base in range(min_base, 11):
        # Interpret the string n_str as base `base`
        value_in_decimal = int(n_str, base)

        # Print the result
        print(f"Interpreting {n_str} in base {base} gives {value_in_decimal} (in base 10).")

def f3_2(n: int) -> None:
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    Using manual computation
    :param n: int in all possible bases
    :return: The result is printed out rather than returned.
    """
    # Special case: if n == 0, then in any base it's still 0
    if n == 0:
        for base in range(2, 11):
            print(f"Interpreting 0 in base {base} gives 0 (in base 10).")
        return
    # Convert n into a string so we can access its digits
    n_str = str(n)

    # Find the maximum digit to determine the minimum base
    max_digit = max(int(d) for d in n_str)
    min_base = max(2, max_digit + 1)
    for base in range(min_base, 11):
        # ---- Manual computation ----
        result = 0
        # Method 1
        # enumerate(reversed(...)) gives us (power, digit)
        # e.g. "2143" → reversed = "3412"
        #   power 0: digit "3" → 3 * base^0
        #   power 1: digit "4" → 4 * base^1
        #   power 2: digit "1" → 1 * base^2
        #   power 3: digit "2" → 2 * base^3
        for power, digit in enumerate(reversed(n_str)):
            result += int(digit) * (base ** power)

        # Method 2
        # Or You can use index from length - i - 1
        # for base in range(min_base, 11):
        #     result = 0
        #     # go left to right, compute power by position
        #     length = len(n_str)
        #     for i in range(length):
        #         digit = int(n_str[i])
        #         power = length - i - 1  # leftmost digit has largest power
        #         result += digit * (base ** power)

        # Print the result
        print(f"Interpreting {n_str} in base {base} gives {result} (in base 10).")