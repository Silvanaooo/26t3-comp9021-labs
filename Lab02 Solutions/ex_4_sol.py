def f4_1(L: list) -> list:
    """
    Remove elements equal to their indices from a list using iteration.

    This is the direct implementation of the problem statement.
    When an element is removed, all subsequent elements shift left,
    changing their indices, which is why we don't increment i after removal.

    :param L: A list of integers (assumed to be in increasing order)
    :return: List: The modified list with elements equal to their indices removed
    """
    i = 0
    while i < len(L):
        if L[i] == i:
            L.pop(i)  # Remove the element at index i
            # Don't increment i since all elements shifted left
        else:
            i += 1  # Element doesn't match its index, move to next
    return L


def f4_2(L: list) -> list:
    """
    Remove elements equal to their indices using a single-pass approach.
    
    This implementation builds a new list by tracking the current index
    after each decision to include/exclude an element. This avoids the
    O(n) cost of pop operations.
    
    Time complexity: O(n)
    Space complexity: O(n) for the result list
    
    :param L: A list of integers (assumed to be in increasing order)
    :return: List: The modified list with elements equal to their indices removed
    """
    result = []
    curr_idx = 0
    
    for val in L:
        if val != curr_idx:
            # Only keep values that don't match their effective index
            result.append(val)
            curr_idx += 1
            
    return result

def f4_3(L: list[int]) -> list[int]:
    """
    Remove elements equal to their indices from a list using a flag.
    :param L: A list of integers (assumed to be in increasing order)
    :return: List: The modified list with elements equal to their indices removed
    """
    while True:
        remove_element = False  # Assume nothing will be removed this round
        for i in range(len(L)):
            if i == L[i]:
                L.pop(i)   # Remove the element
                remove_element = True
                break      # Restart loop after removal
        if not remove_element:    # No removal this round -> stop
            break
    return L