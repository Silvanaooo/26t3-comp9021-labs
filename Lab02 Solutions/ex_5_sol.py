def f5_1(L: list[int]) -> dict[int, tuple]:
    """
    Find elements that are between their circular neighbors in value.

    For each element in the list, checks if it falls between its previous
    and next neighbors in value (not index). If so, adds the element as a
    key in the result dictionary with a tuple of (min_neighbor, max_neighbor)
    as the value.

    :param L: (int) A list of integers
    :return: (Dict[int, tuple]) Dictionary mapping qualified elements to tuples of their min and max neighbors
    """
    D = {}
    for i in range(len(L)):
        prev_val = L[i - 1]  # Previous element (wraps to last element for first position)
        next_val = L[(i + 1) % len(L)]  # Next element (wraps to first element for last position)
        if prev_val > next_val:
            prev_val, next_val = next_val, prev_val  # Ensure m is the smaller value and n is the larger
        if prev_val < L[i] < next_val:
            D[L[i]] = (prev_val, next_val)  # Element is between its neighbors in value
    return D


def f5_2(L: list[int]) -> dict[int, tuple]:
    """
    Find elements between their circular neighbors using an extended list approach.
    
    Creates a temporary extended list by appending the first two elements to the end,
    which simplifies circular access. This avoids using modulo arithmetic
    at the cost of slightly more memory.
    
    :param L: (int) A list of integers
    :return: (Dict[int, tuple]) Dictionary mapping qualified elements to tuples of their min and max neighbors
    """
    # Create extended list with wrap-around elements
    extended_L = [L[-1]] + L + [L[0]] # or use slicing: extended_L = L[-1:] + L + L[:1]
    result = {}
    
    for i in range(len(L)):
        prev_val = extended_L[i]      # Previous element
        curr_val = extended_L[i+1]    # Current element
        next_val = extended_L[i+2]    # Next element
        
        neighbors = [prev_val, next_val]
        min_neighbor = min(neighbors)
        max_neighbor = max(neighbors)
        
        if min_neighbor < curr_val < max_neighbor:
            result[curr_val] = (min_neighbor, max_neighbor)
            
    return result