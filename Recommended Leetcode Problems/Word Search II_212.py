def find_words(board, words):
    """
    Given a 2D board and a list of words, return all words that can be
    formed by moving up, down, left, or right, using each cell at most once.

    This uses the same DFS + path + backtracking style as in the paths() example.

    Example:
        >>> board = [
        ...   ["A","B","C","E"],
        ...   ["S","F","C","S"],
        ...   ["A","D","E","E"]
        ... ]
        >>> sorted(find_words(board, ["ABCCED", "SEE", "ABCB"]))
        ['ABCCED', 'SEE']
    """
    # Edge cases
    if not board or not board[0] or not words:
        return []

    height = len(board)
    width = len(board[0])

    # 4 directions: up, down, left, right
    directions = [
        (-1, 0),  # North
        (1, 0),   # South
        (0, -1),  # West
        (0, 1),   # East
    ]

    found = set()

    def has_path(word):
        """
        Return True if there is at least one path in the board
        that spells out `word`. Internally it collects all paths,
        in the same style as paths().
        """
        # Quick impossible case
        if len(word) > height * width:
            return False

        # For this word, we have our own visited matrix
        visited = [[False for _ in range(width)] for _ in range(height)]
        solutions = []

        def dfs(x, y, index, path):
            # Base case: we just matched the last character
            if index == len(word) - 1:
                # Current path is a complete solution for this word
                solutions.append(path[:])
                return

            # Otherwise, explore in all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width:
                    if board[nx][ny] == word[index + 1] and not visited[nx][ny]:
                        path.append((nx, ny))
                        visited[nx][ny] = True
                        dfs(nx, ny, index + 1, path)
                        path.pop()
                        visited[nx][ny] = False

        # Try to start from every cell that matches the first character
        for r in range(height):
            for c in range(width):
                if board[r][c] == word[0]:
                    dfs(r, c, 0, [])

        return bool(solutions)

    # For each word in the list, check if it has a path
    for w in words:
        if has_path(w):
            found.add(w)

    return list(found)