def f3_1(L: list[int]) -> None:
    """
    Removes elements from L using a while loop and remove method.
    Checks from right to left, removing elements smaller than their successors.
    """
    while len(L) > 1 and L[-2] < L[-1]:
        L.remove(L[-2])
    print(L)


def f3_2(L: list[int]) -> None:
    """
    Removes elements from L using a while loop and remove method.
    Checks from right to left, removing elements smaller than their successors.
    Uses TWO loops (one backward scan + one filter) but overall O(n).
    Prints the filtered list.
    """
    e = L[-1]  # last element
    to_delete = set()  # values to remove

    # collect suffix values < e
    i = len(L) - 2
    while L[i] < e:
        to_delete.add(L[i])
        i -= 1

    # filter them out from the list
    result = [x for x in L if x not in to_delete]
    print(result)


def f3_3(L: list[int]) -> None:
    """
    Removes elements from L using a while loop and remove method.
    Checks from right to left, removing elements smaller than their successors.
    """
    if len(L) <= 1:
        print(L)
        return

    e = L[-1]  # get the last element e

    i = len(L) - 2  # index for second last element in L and move leftwards later in the while loop
    to_remove = []  # collect all x

    # scan from the end as long as L[i] < e
    while L[i] < e:
        to_remove.append(L[i])
        i = i - 1

    result = []  # build new list to keep numbers not in to_remove

    for num in L:
        if num not in to_remove:
            result.append(num)

    print(result)