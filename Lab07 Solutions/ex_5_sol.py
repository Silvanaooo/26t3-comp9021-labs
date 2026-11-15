# Call special list a list whose members are integers or special lists.
# Assume that the argument L is a special list.
#
# If the returned dictionary contains a key of the form (i_1, ..., i_n),
# with as associated value the integer e, then:
# - if n == 1 then the member of L of index i_1 is e;
# - if n == 2 then the member of L of index i_1 is a
#   list L1, and the member of L1 of index i_2 is e;
# - if n == 3 then the member of L of index i_1 is a
#   list L1, and the member of L1 of index i_2 is a
#   list L2, and the member of L2 of index i_3 is e;
# ...
#
# isinstance() is useful.

def f5_1(L):
    """
    Converts a special list (containing integers or other special lists) into a dictionary.

    The dictionary maps tuples of indices to integer values, where each tuple represents
    the path to an integer in the nested list structure:
    - A key (i,) maps to an integer at index i in the top-level list
    - A key (i, j) maps to an integer at index j in a sublist at index i
    - A key (i, j, k) maps to an integer at index k in a sublist at index j in a sublist at index i
    - And so on for deeper nesting levels

    This implementation uses recursion to traverse the nested list structure.

    Args:
        L: A special list containing integers or other special lists

    Returns:
        A dictionary mapping index paths (as tuples) to integer values

    Example:
        f5_1([1, [2, 3], 4]) returns {(0,): 1, (1, 0): 2, (1, 1): 3, (2,): 4}
    """
    result = {}

    # Iterate through each element in the list
    for i in range(len(L)):
        # If the element is an integer, add it to the result with its index as a tuple
        if isinstance(L[i], int):
            result[(i,)] = L[i]
        # If the element is a list, recursively process it
        else:
            # Get the dictionary for the nested list
            nested_dict = f5_1(L[i])
            # Add each entry from the nested dictionary to the result,
            # prepending the current index to each key
            for indices, value in nested_dict.items():
                result[(i,) + indices] = value

    return result

def def5_2(L):
    D = {}  # Result: {tuple(path): integer_value}

    def dfs(node, path):
        """
        node: current position in the structure (either an int or a list).
        path: list of indexes from the root to 'node' (e.g., [1, 0, 2]).
        """

        # If 'node' is an integer, we reached a leaf.
        # Record the mapping from the current path to this value.
        # Use tuple(path) because dict keys must be immutable and hashable.
        #
        # Note: in Python, bool is a subclass of int. If you do NOT want to
        # treat True/False as integers here, replace the check with:
        #     if type(node) is int:
        if isinstance(node, int):
            D[tuple(path)] = node
            return  # Leaf handled; stop descending.

        # Otherwise, assume 'node' is a list (another level in the nesting).
        # Visit each child. The child's index 'i' is appended to the path.
        # 'path + [i]' creates a new list; we do not need to backtrack/pop.
        for i in range(len(node)):
            dfs(node[i], path + [i])

    # Start DFS at the root with an empty path.
    dfs(L, [])

    # Return the completed mapping.
    return D
