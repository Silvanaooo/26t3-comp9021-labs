def f4_1(D: dict[int, int], n: int) -> list[int]:
    """
    Uses a while loop to iteratively build the sequence.
    Use simple and direct non-recursive implementation.
    """
    if n not in D:
        return []
    
    L = [n]
    while n in D and n < D[n]:
        n = D[n]
        L.append(n)
    
    return L


def f4_2(D: dict[int, int], n: int) -> list[int]:
    """
    Uses recursion to build the sequence.
    Base case is when n is not in D.
    Always includes D[n] if n is in D.
    """
    # Base case: stop if n is not a key in D
    if n not in D:
        return []

    # Get the next value
    next_val = D[n]

    # Continue only if the sequence is strictly increasing
    if n < next_val:
        if next_val in D:
            # Recursive call: extend the sequence from next_val
            rest_of_sequence = f4_2(D, next_val)
            return [n] + rest_of_sequence
        else:
            # End of chain: include n and next_val
            return [n, next_val]
    else:
        # If sequence does not increase, stop with just n
        return [n]