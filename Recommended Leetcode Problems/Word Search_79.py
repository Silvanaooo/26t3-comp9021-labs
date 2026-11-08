class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        LeetCode 79. Word Search

        Use DFS with backtracking to determine if the given word
        can be constructed in the grid. Each step can move in one
        of four directions (up, down, left, right), and each cell
        can be used at most once in a given path.

        Args:
            board: 2D list of characters.
            word:  String to search for.

        Returns:
            bool: True if the word exists, otherwise False.

        Example:
            >>> s = Solution()
            >>> board = [
            ...   ["A","B","C","E"],
            ...   ["S","F","C","S"],
            ...   ["A","D","E","E"]
            ... ]
            >>> s.exist(board, "ABCCED")
            True
            >>> s.exist(board, "SEE")
            True
            >>> s.exist(board, "ABCB")
            False
        """
        if not board or not board[0] or not word:
            return False

        height = len(board)
        width = len(board[0])
        visited = [[False for _ in range(width)] for _ in range(height)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x: int, y: int, index: int) -> bool:
            # All characters matched
            if index == len(word):
                return True
            # Out of bounds
            if x < 0 or y < 0 or x >= height or y >= width:
                return False
            # Wrong character or already visited
            if visited[x][y] or board[x][y] != word[index]:
                return False

            # Mark current cell as visited
            visited[x][y] = True

            # Explore all 4 directions
            for i, j in directions:
                dx, dy = x + i, y + j
                if dfs(dx, dy, index + 1):
                    return True

            # Backtrack
            visited[x][y] = False
            return False

        for r in range(height):
            for c in range(width):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False

def print_word_path(board: list[list[str]], word: str) -> None:
    """
    Find the path of `word` in `board` using DFS + backtracking and print it.
    Path cells are printed as their original letters; all other cells as `blank`.

    Coordinates:
        x = row index (down), y = col index (right). Movement is 4-directional.

    Args:
        board: 2D list of single-character strings.
        word:  string to search for.
        mode:  "full"   -> print a full-size mask (same rows/cols as board, no rstrip)
               "cropped"-> print cropped to the minimal bounding box (rstrip each line)
        blank: placeholder for non-path cells (default: space)

    Examples (doctest style):

        >>> b = [
        ...   ["A","B","C","E"],
        ...   ["S","F","C","S"],
        ...   ["A","D","E","E"]
        ... ]
        >>> print_word_path(b, "ABCCED")
        ABC
          C
         DE
        >>> print_word_path(b, "ABCB")
        Not found.
    """
    # Basic validation
    if not board or not board[0] or not word:
        print("Not found.")
        return

    height = len(board)
    width = len(board[0])

    # DFS + backtracking to collect a path

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path = []

    visited = [[False for _ in range(width)] for _ in range(height)]
    def dfs(x: int, y: int, index: int) -> bool:
        # Index points to the character we must match at (x, y)
        if index == len(word):
            return True
        if x < 0 or y < 0 or x >= height or y >= width:
            return False
        if visited[x][y] or board[x][y] != word[index]:
            return False

        visited[x][y] = True
        path.append((x, y))

        for i, j in directions:
            dx, dy = x + i, y + j
            if dfs(dx, dy, index + 1):
                return True

        # Backtrack if all branches fail
        visited[x][y] = False
        path.pop()
        return False


    # =============================================================================================
    # Or instead of keeping a separate visited matrix, we can simply test if (x, y) is in path list to test
    # if we visited that coordinates or not.
    # =============================================================================================
    # def dfs(x, y, index):
    #     if index == len(word):
    #         return True
    #     if x < 0 or y < 0 or x >= height or y >= width:
    #         return False
    #     if (x, y) in path or board[x][y] != word[index]:
    #         return False
    #
    #     path.append((x, y))
    #     for i, j in directions:
    #         dx, dy = x + i, y + j
    #         if dfs(dx, dy, index + 1):
    #             return True
    #     path.pop()
    #     return False
    # =============================================================================================

    # Try every cell as a start, but only where the first letter matches
    found = False
    for i in range(height):
        for j in range(width):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    found = True
                    break
        if found:
            break

    if not found:
        print("Not found.")
        return

    # Printing section
    xs = [x for x, _ in path]
    ys = [y for _, y in path]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    path_set = set(path)

    for x in range(min_x, max_x + 1):
        row_chars = []
        for y in range(min_y, max_y + 1):
            row_chars.append(board[x][y] if (x, y) in path_set else " ")
        print("".join(row_chars).rstrip())