def num_enclaves_dfs(grid) -> int:
    """
    LeetCode 1020. Number of Enclaves (DFS, with visited T/F matrix; no mutation)

    Count land cells ('1') that cannot reach the boundary by moving 4-directionally.
    Idea:
      1) From all boundary land cells, DFS-mark them as `visited=True`.
      2) Any land cell not visited after step #1 is an enclave. Count them.

    Notes:
      - Works whether grid uses int 0/1 or str "0"/"1".
      - Does NOT mutate the grid.

    Args:
        grid: 2D list with 0/1 or "0"/"1"

    Returns:
        int: number of enclave land cells.

    Examples:
        >>> g1 = [
        ...   [0,0,0,0],
        ...   [1,0,1,0],
        ...   [0,1,1,0],
        ...   [0,0,0,0]
        ... ]
        >>> num_enclaves_dfs(g1)
        3
        >>> g2 = [
        ...   [0,1,1,0],
        ...   [0,0,1,0],
        ...   [0,0,1,0],
        ...   [0,0,0,0]
        ... ]
        >>> num_enclaves_dfs(g2)
        0
    """
    if not grid or not grid[0]:
        return 0

    height = len(grid)
    width = len(grid[0])
    visited = [[False for _ in range(width)] for _ in range(height)]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    def dfs(x: int, y: int) -> None:
        # Base cases
        if x < 0 or x >= height or y < 0 or y >= width:
            return
        if grid[x][y] == 0 or visited[x][y]:
            return
        visited[x][y] = True
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    # Step 1: mark all land reachable from the boundary
    for j in range(width):
        if grid[0][j] == 1:
            dfs(0, j)
        if grid[height - 1][j] == 1:
            dfs(height - 1, j)
    for i in range(height):
        if grid[i][0] == 1:
            dfs(i, 0)
        if grid[i][width - 1] == 1:
            dfs(i, width - 1)

    # Step 2: count unvisited land
    enclaves = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1 and not visited[i][j]:
                enclaves += 1
    return enclaves



def num_enclaves_mark_inplace(grid, restore: bool = False) -> int:
    """
    DFS in-place marking version:
      - From all boundary land cells (1), mark their component as 2
      - Count remaining 1's as enclaves
      - Optionally restore all 2 -> 1

    Args:
        grid: 2D list of ints (0/1)
        restore: If True, revert 2 back to 1 after counting

    Example:
        >>> g = [
        ...   [0,0,0,0],
        ...   [1,0,1,0],
        ...   [0,1,1,0],
        ...   [0,0,0,0]
        ... ]
        >>> num_enclaves_mark_inplace(g)
        3
    """
    if not grid or not grid[0]:
        return 0

    height = len(grid)
    width = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs_mark(x: int, y: int) -> None:
        if x < 0 or x >= height or y < 0 or y >= width:
            return
        if grid[x][y] != 1:
            return
        grid[x][y] = 2
        for dx, dy in directions:
            dfs_mark(x + dx, y + dy)

    # Step 1: mark from all boundary land cells
    for j in range(width):
        if grid[0][j] == 1:
            dfs_mark(0, j)
        if grid[height - 1][j] == 1:
            dfs_mark(height - 1, j)
    for i in range(height):
        if grid[i][0] == 1:
            dfs_mark(i, 0)
        if grid[i][width - 1] == 1:
            dfs_mark(i, width - 1)

    # Step 2: count remaining 1's as enclaves
    count = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                count += 1

    # Optional restore
    if restore:
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    grid[i][j] = 1

    return count