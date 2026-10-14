def f3_1(L: list) -> list:
    """
    Removes elements from a list where the element is the arithmetic mean of its neighbors.

    Iterates through the list and removes any element that is equal to the average
    of its immediate neighbors (i.e., where L[i] = (L[i-1] + L[i+1])/2).
    Continues this process until no more elements can be removed.

    :param L: A list of numbers
    :return: The modified list with arithmetic mean elements removed
    """
    # Initialize index
    i = 0
    
    # Iterate through the list with walrus operator to increment i
    while (i := i + 1) < len(L) - 1:
        # Check if current element is arithmetic mean of neighbors
        if L[i - 1] + L[i + 1] == L[i] * 2:
            # Remove the current element
            L.pop(i)
            # Decrement index since we removed an element
            i -= 1
            
    # Return the modified list
    return L

def f3_2(L: list) -> list:
    """
    Removes elements from a list where the element is the arithmetic mean of its neighbors.

    Iterates through the list and removes any element that is equal to the average
    of its immediate neighbors (i.e., where L[i] = (L[i-1] + L[i+1])/2).
    Continues this process until no more elements can be removed.

    :param L: A list of numbers
    :return: The modified list with arithmetic mean elements removed
    """
    if len(L) < 3:
        return L

    while True:
        removed = False
        # scan from left to right, only interior indices
        for i in range(1, len(L) - 1):
            if L[i - 1] + L[i + 1] == 2 * L[i]:
                L.pop(i)      # remove the leftmost such element
                removed = True
                break         # restart a new pass from the left
        if not removed:
            break
    return L


def f3_3(L: list) -> list:
    """
    Removes elements from a list where the element is the arithmetic mean of its neighbors.

    Iterates through the list and removes any element that is equal to the average
    of its immediate neighbors (i.e., where L[i] = (L[i-1] + L[i+1])/2).
    Continues this process until no more elements can be removed.

    :param L: A list of numbers
    :return: The modified list with arithmetic mean elements removed
    """
    # Create a copy to avoid modifying the input list directly
    result = L.copy()
    
    # Continue until no more elements can be removed
    changed = True
    while changed and len(result) > 2:
        changed = False
        
        # Iterate through the list backwards to avoid index shifting problems
        i = len(result) - 2
        while i > 0:
            # Check if current element is arithmetic mean of neighbors
            if result[i - 1] + result[i + 1] == result[i] * 2:
                # Remove the current element
                result.pop(i)
                changed = True
            i -= 1
    
    # Return the modified list
    return result

