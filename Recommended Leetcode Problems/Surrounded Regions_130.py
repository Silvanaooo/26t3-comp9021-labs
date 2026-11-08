def solve_surrounded_regions(board: list[list[str]]) -> None:
    """
    Modify the board in-place:
    Flip every 'O' that is fully surrounded by 'X' into 'X'.
    Keep 'O's that are connected to the boundary as 'O'.

    Idea:
      1) DFS from all boundary 'O's and mark them as 'S' (safe).
      2) Scan the board:
           - flip remaining 'O' -> 'X' (captured)
           - flip 'S' -> 'O'    (restore safe cells)

    Examples (doctest):

        >>> b = [["X","X","X","X"],
        ...      ["X","O","O","X"],
        ...      ["X","X","O","X"],
        ...      ["X","O","X","X"]]
        >>> solve_surrounded_regions(b)
        >>> b
        [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]

        # Edge: single cell
        >>> b2 = [["O"]]
        >>> solve_surrounded_regions(b2)
        >>> b2
        [['O']]

        # All O's touching boundary should remain O
        >>> b3 = [["O","O"],
        ...       ["O","O"]]
        >>> solve_surrounded_regions(b3)
        >>> b3
        [['O', 'O'], ['O', 'O']]

        # Mixed case, boundary-connected arms remain
        >>> b4 = [["X","O","X"],
        ...       ["O","X","O"],
        ...       ["X","O","X"]]
        >>> solve_surrounded_regions(b4)
        >>> b4
        [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
    """
    if not board or not board[0]:
        return

    height = len(board)
    width = len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs_mark(x: int, y: int) -> None:
        """
        Mark boundary-reachable 'O' as 'S' (safe).
        """
        if x < 0 or x >= height or y < 0 or y >= width:
            return
        if board[x][y] != 'O':
            return
        board[x][y] = 'S'
        for dx, dy in directions:
            dfs_mark(x + dx, y + dy)

    # 1) Flood-fill from boundary 'O's
    # Top and bottom rows
    for j in range(width):
        if board[0][j] == 'O':
            dfs_mark(0, j)
        if board[height - 1][j] == 'O':
            dfs_mark(height - 1, j)
    # Left and right columns
    for i in range(height):
        if board[i][0] == 'O':
            dfs_mark(i, 0)
        if board[i][width - 1] == 'O':
            dfs_mark(i, width - 1)

    # 2) Flip captured and restore safe
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'O':
                board[i][j] = 'X'   # captured
            elif board[i][j] == 'S':
                board[i][j] = 'O'   # restore