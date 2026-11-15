def f2():
    """
    Generates rows of Pascal's triangle as an infinite sequence.
    
    Pascal's triangle is a triangular array where each number is the sum of the
    two numbers directly above it. The first row is [1], and each subsequent row
    starts and ends with 1, with each internal element being the sum of the two
    elements above it.
    
    This implementation uses list comprehension to efficiently calculate each new row
    based on the previous row.
    
    Returns:
        A generator that yields each row of Pascal's triangle as a list of integers
    
    Example:
        First few rows of Pascal's triangle:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
    """
    # Start with the first row of Pascal's triangle
    current_row = [1]
    yield current_row
    
    # Infinite loop to generate subsequent rows
    while True:
        # Create the next row using list comprehension:
        # - Start with 1
        # - Add pairs of adjacent elements from the current row
        # - End with 1
        current_row = [1] + [current_row[i] + current_row[i + 1] 
                            for i in range(len(current_row) - 1)] + [1]
        yield current_row
