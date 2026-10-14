def f4_1(n: int) -> None:
    """
    Expresses an integer as a sum of powers of 2 (binary representation).
    
    Converts the number to binary, then interprets each '1' bit as the corresponding
    power of 2. For example, 42 (101010 in binary) is expressed as 2^5 + 2^3 + 2^1.
    Negative numbers are expressed as the negative of the powers sum.
    
    Args:
        n: An integer to express as sum of powers of 2
    """
    # Handle the special case of 0
    if not n:
        print('0 = 0')
        return
        
    # Convert number to binary representation without '0b' prefix
    binary_n = f'{n:b}'
    
    # Extract positions where binary digits are '1'
    # Reversed to process from most significant to least significant bit
    powers = (i for i in range(len(binary_n)) if binary_n[i] == '1')
    
    # Determine the operator based on sign of n
    operator = ' + ' if n >= 0 else ' - '
    
    # Print the number and equal sign (with negative sign if needed)
    print(n, '= ', end='' if n > 0 else '-')
    
    # Print the sum of powers of 2, joining with the appropriate operator
    # The power is calculated as (length of binary - position - 1)
    print(operator.join(f'2^{len(binary_n) - i - 1}' for i in powers))


def f4_2(n: int) -> None:
    """
    Print n as a sum of powers of 2, e.g. 42 = 2^5 + 2^3 + 2^1.
    For negative n, print a leading minus on the whole sum, e.g. -5 = -2^2 - 2^0.
    """
    # Special case: 0
    if n == 0:
        print('0 = 0')
        return

    # Work with the absolute value when extracting bits
    m = abs(n)
    binary_m = f'{m:b}'  # e.g. 42 -> '101010'

    # Collect powers where the bit is '1' (from most significant to least)
    powers = []
    for i in range(len(binary_m)):
        if binary_m[i] == '1':
            # The leftmost bit represents the highest power,
            # so to find the correct exponent, we count backward from the end.
            power = len(binary_m) - i - 1
            powers.append(power)      # e.g. [5, 3, 1]

    # Build the textual expression from collected powers
    terms = [f'2^{p}' for p in powers]

    if n > 0:
        expr = ' + '.join(terms)
        print(f'{n} = {expr}')
    else:
        # For negatives, print a leading minus and join with ' - '
        expr = ' - '.join(terms)
        print(f'{n} = -{expr}')