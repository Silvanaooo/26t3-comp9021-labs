# Assume that the argument L is a list of lists of integers

def f1_1(L: list[list[int]]) -> tuple[list[int], list[list[int]]]:
    """
    Flattens and sorts all elements from a list of lists, then regroups
    the sorted elements based on the original sublist lengths.

    Args:
        L: A list where each element is a list of integers.

    Returns:
        A tuple containing two lists:
        1. F: A single list with all integers from L, sorted.
        2. R: A list of lists, where sorted elements are regrouped
           according to the original lengths of sublists in L.
    """
    # Calculate the lengths of each sublist in the input list L.
    # e.g., if L = [[3, 1], [2]], lengths will be [2, 1]
    lengths = [len(L1) for L1 in L]

    # Flatten the list of lists L into a single list and sort it.
    # The list comprehension (e for L1 in L for e in L1) iterates through
    # each sublist (L1) and then each element (e) in that sublist.
    # sorted() then sorts the resulting flat list.
    # e.g., if L = [[3, 1], [2]], F will be [1, 2, 3]
    F = sorted(e for L1 in L for e in L1)

    # Reconstruct the list of lists R using the sorted elements F
    # and the original lengths.
    R = []
    # Keep track of the starting index for slicing F.
    i = 0
    # Iterate 'n' from 0 up to the number of original sublists.
    # In each iteration, 'n' corresponds to the index of the length
    # we need to use from the 'lengths' list.
    for n in range(len(L)):
        # Append a slice of F to R.
        # The slice starts at index 'i'.
        # The slice ends at index 'i + lengths[n]'.
        # The walrus operator (:=) updates 'i' in place for the next iteration.
        # It assigns the value of 'i + lengths[n]' to 'i' *after* the
        # original value of 'i' is used for the slice's end index.
        # 1st iteration (n=0): L=[[3, 1], [2]], lengths=[2, 1], F=[1, 2, 3], i=0
        #   Slice F[0 : (i := 0 + 2)] -> F[0:2] which is [1, 2]. i becomes 2. R = [[1, 2]]
        # 2nd iteration (n=1): lengths[1]=1, i=2
        #   Slice F[2 : (i := 2 + 1)] -> F[2:3] which is [3]. i becomes 3. R = [[1, 2], [3]]
        R.append(F[i : (i := i + lengths[n])])

    # Return the sorted flat list F and the reconstructed list R.
    return F, R


def f1_2(L: list[list[int]]) -> tuple[list[int], list[list[int]]]:
    """
    Flattens and sorts all elements from a list of lists, then regroups
    the sorted elements based on the original sublist lengths.

    This version uses explicit index tracking instead of the walrus operator.

    Args:
        L: A list where each element is a list of integers.

    Returns:
        A tuple containing two lists:
        1. F: A single list with all integers from L, sorted.
        2. R: A list of lists, where sorted elements are regrouped
           according to the original lengths of sublists in L.
    """

    # Get the lengths of each sublist
    lengths = [len(sublist) for sublist in L]

    # Flatten all numbers and sort them
    # This is a double for-loop in one line:
    # "for sublist in L" and then "for e in sublist"
    new_l = sorted(e for sublist in L for e in sublist)

    # Split F into sublists matching the original lengths
    result = []
    i = 0  # starting index
    for n in range(len(L)):
        next_i = i + lengths[n]    # compute next cutoff
        result.append(new_l[i:next_i])      # slice this portion
        i = next_i                 # update the starting index

    return new_l, result