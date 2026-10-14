def f6_1(*L) -> list:
    """
    Creates a structured list by reorganizing elements from the input sequence and its reverse.
    
    This function uses zip operations to create a specific pattern of nested tuples:
    1. First creates pairs from original elements and their mirrored positions
    2. Then uses zip with unpacking to reorganize these pairs in a specific pattern
    
    :param L: Variable-length argument list of integers
    :return: A list of two tuples showing symmetric unpacking patterns
    """
    # Create two zipped sequences:
    # 1. Original elements paired with reversed elements
    # 2. Reversed elements paired with original elements
    original_with_reversed = zip(L, reversed(L))
    reversed_with_original = zip(reversed(L), L)
    
    # When unpacked with *, zip(L, reversed(L)) provides pairs of elements as arguments to the outer zip
    # This is equivalent to: zip((L[0], rev_L[0]), (L[1], rev_L[1]), ..., (L[n-1], rev_L[n-1]))
    # The outer zip will group all first elements and all second elements, creating:
    # [(L[0], L[1], ..., L[n-1], rev_L[0], rev_L[1], ..., rev_L[n-1]), 
    #  (rev_L[0], rev_L[1], ..., rev_L[n-1], L[0], L[1], ..., L[n-1])]
    return list(zip(*original_with_reversed, *reversed_with_original))


def f6_2(*L: int) -> list[tuple[int, ...]]:
    """
    Demonstrates how to use unpacking (*) together with reversed()
    to build mirrored tuples from an arbitrary number of integers.

    1. Inside the function definition, *L packs all input arguments into a tuple.
    2. Inside the return expression, *L and *reversed(L) unpack values again
       — the first unpacks the tuple, the second unpacks a reversed iterator.

    This function creates two tuples:
    1. The first tuple concatenates all elements of L followed by their reversed order.
    2. The second tuple does the opposite: reversed elements first, then the original ones.

    It illustrates how * (unpacking) can expand iterable elements directly inside a tuple.
    Only *, list, and reversed are used — no loops or comprehensions.

    :param L: Variable-length argument list of integers
    :return: A list of two tuples showing symmetric unpacking patterns
    """
    if not L:
        return []
    # Step 1: Use unpacking (*) to expand all elements of L.
    # Step 2: reversed(L) produces an iterator of the same elements in reverse order.
    # Step 3: Combine both using tuple literals and unpacking.
    #   - (*L, *reversed(L))  → concatenates L then reversed(L)
    #   - (*reversed(L), *L)  → concatenates reversed(L) then L
    return [(*L, *reversed(L)), (*reversed(L), *L)]

def f6_3(*L) -> list:
    """
    Creates a structured list by directly constructing the result tuples.
    
    This implementation explicitly builds the output format without nested zip operations,
    making it easier to understand the transformation being performed.
    
    :param L: Variable-length argument list of integers
    :return: A list of two tuples showing symmetric unpacking patterns
    """
    # Convert arguments to a list for easier manipulation
    elements = list(L)
    
    # Handle empty input
    if not elements:
        return []
    
    # Create reversed elements once
    reversed_elements = list(reversed(elements))
    
    # Directly construct the two result tuples:
    # First tuple: all original elements followed by all reversed elements
    first_tuple = tuple(elements + reversed_elements)
    
    # Second tuple: all reversed elements followed by all original elements
    second_tuple = tuple(reversed_elements + elements)
    
    # Return both tuples in a list
    return [first_tuple, second_tuple]