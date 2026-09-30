def f3_1(L: list) -> list:
    """
    Remove matching elements from both ends of the list until they no longer match.

    This implementation uses list.pop() operations which are O(n) for pop(0).

    :param L (list): The input list to process
    :return: list: The modified list with matching end elements removed
    """
    while len(L) > 1 and L[0] == L[-1]:
        L.pop(0)  # O(n) operation - must shift all elements
        L.pop()   # O(1) operation - removes from the end
    return L


def f3_2(L: list) -> list:
    """
    Remove matching elements from both ends of the list using deque.
    
    :param L (list): The input list to process
    :return: list: The modified list with matching end elements removed
    """
    from collections import deque
    # Convert to deque for efficient operations at both ends, .popleft(), .pop()
    d = deque(L)
    while len(d) > 1 and d[0] == d[-1]:
        d.popleft()  # O(1) operation
        d.pop()      # O(1) operation
    return list(d)