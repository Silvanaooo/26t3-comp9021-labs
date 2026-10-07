def f4_1(n: int, base: int) -> dict[int, tuple[int]]:
    """
    Creates a dictionary mapping integers from 0 to n to their representation in the specified base.
    
    Uses iterative division by base to convert decimal numbers to the target base.

    :param n: The upper limit of numbers to convert (inclusive)
    :param base: The target base (between 2 and 9)
    :return: A dictionary where keys are integers from 0 to n and values are tuples
        representing those numbers in the specified base
    """
    # Initialize dictionary with special case for 0
    D = {0: (0,)}
    
    # Process each number from 1 to n
    for m in range(1, n + 1):
        digits = []  # List to store digits in reverse order
        p = m  # Working copy of the number
        
        # Convert decimal to the specified base
        # Keep dividing by base until the quotient is 0
        while p > 0:
            remainder = p % base  # Get remainder (current digit)
            digits.append(remainder) # Store it
            p //= base  # Update quotient for next step
            
        # Reverse digits to get correct order and convert to tuple
        D[m] = tuple(reversed(digits))

    return D

def f4_2(n: int, base: int) -> dict[int, tuple[int]]:
    """
    Creates a dictionary mapping integers from 0 to n to their representation in the specified base.
    
    Uses Python's divmod function for cleaner code and more efficient conversion.
    
    :param n: The upper limit of numbers to convert (inclusive)
    :param base: The target base (between 2 and 9)
    :return: A dictionary where keys are integers from 0 to n and values are tuples
        representing those numbers in the specified base
    """
    result = {}
    
    # Handle special case for 0
    result[0] = (0,)
    
    # Process each number from 1 to n
    for num in range(1, n + 1):
        digits = []
        temp = num
        
        # Convert using divmod for cleaner code
        while temp > 0:
            # divmod returns quotient and remainder in one operation
            temp, remainder = divmod(temp, base)
            digits.append(remainder)
            
        # Reverse digits and convert to tuple
        result[num] = tuple(reversed(digits))
        
    return result