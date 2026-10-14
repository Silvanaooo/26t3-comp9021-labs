def f2_1(S: set) -> list[set]:
    """
    Creates a list of sets by progressively removing the maximum element
    from a copy of the input set.

    Starting with the original set, creates a sequence where each subsequent set
    is derived by removing the maximum element from the previous set.

    :param S: A non-empty set of integers

    Returns:
        A list of sets, starting with the original set and ending with a set containing
        only the minimum element
    """
    # Create a working copy so the original input set is not modified
    # here we use set constructor to do shallow copy
    # you can also use 
    # Method 2: copy() method current_set = S.copy()
    current_set = set(S)

    # Create the first element of the result list - a copy of the original set
    U = [set(current_set)]

    # Continue until only one element remains in the working set
    while len(current_set) > 1:
        # Remove the maximum element from the working set
        current_set.remove(max(current_set))
        # Add a copy of the modified set to the result list
        U.append(set(current_set))

    # Return the list containing all sets
    return U


def f2_2(S: set) -> list[set]:
    """
    Creates a list of sets by iteratively generating subsets of decreasing size.

    Uses a sorted list approach to create a sequence of sets where each set
    contains all remaining elements except the largest ones already removed.

    :param S: A non-empty set of integers

    Returns:
        A list of sets, starting with the original set and ending with a set containing
        only the minimum element
    """
    # Sort the elements of the set in increasing order
    sorted_elements = sorted(S)

    # Initialize the result list
    result = []

    # Repeatedly convert the current list of remaining elements into a set
    while sorted_elements:
        # Create a set from all current remaining elements
        result.append(set(sorted_elements))
        # Remove the largest element from the list
        sorted_elements.pop()

    # Return the list of sets
    return result


def f2_3(S: set) -> list[set]:
    """
    Creates a list of sets using a recursive approach to generate the sequence.

    Recursively builds the list by removing the maximum element at each step,
    while preserving the original input set.

    :param S: A non-empty set of integers

    Returns:
        A list of sets, starting with the original set and ending with a set containing
        only the minimum element
    """
    # Base case: if the set has only one element, return a list with a copy of that set
    if len(S) == 1:
        return [set(S)]

    # Create a copy of the set so the original input is not modified
    smaller_set = set(S)

    # Remove the maximum element from the copied set
    smaller_set.remove(max(smaller_set))

    # Return the original set first, followed by the recursive result
    return [set(S)] + f2_3(smaller_set)