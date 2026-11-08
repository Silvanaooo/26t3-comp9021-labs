def island_area_at_dfs(grid, i, j) -> int:
    """
    Compute the area (number of land cells) of the island that contains (r0, c0),
    using recursive DFS.

    If the starting cell is water ('0') or out of bounds, return 0.

    Args:
        grid: A 2D list of "0" and "1" characters.
        r0, c0: Starting row and column.

    Returns:
        int: The number of land cells in this island.

    Example:
        >>> g = [
        ...   ["1","1","0"],
        ...   ["1","1","0"],
        ...   ["0","0","1"],
        ...   ["0","1","1"]
        ... ]
        >>> island_area_at_dfs(g, 0, 0)
        4
        >>> island_area_at_dfs(g, 2, 2)
        3
        >>> island_area_at_dfs(g, 3, 2)
        3
    """
    if not grid or not grid[0]:
        return 0
    height = len(grid)
    width = len(grid[0])
    if not (0 <= i < height and 0 <= j < width):
        return 0
    if grid[i][j] != "1":
        return 0

    visited = [[False] * width for _ in range(height)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x: int, y: int) -> int:
        # Base cases, if the point out of scope we return 0
        if x < 0 or x >= height or y < 0 or y >= width:
            return 0
        if grid[x][y] == "0" or visited[x][y]:
            return 0

        visited[x][y] = True
        area = 1  # use to count current cell
        for i, j in directions:
            dx, dy = x + i, y + j
            area += dfs( dx, dy)
        return area

    area = dfs(i, j)

    return area


def print_island_at_dfs(grid, i, j) -> None:
    """
    Print the FULL-SIZE map (same size as input grid) of the island that contains (i, j),
    using recursive DFS.

    The island is shown with `fill` (default '*'), and all non-island cells in the full
    grid are printed as `blank` (default ' ' — a space). This function does not mutate
    the input grid.

    If the starting cell is water ('0') or out of bounds, print a message and return.

    Args:
        grid: A 2D list of "0" and "1" characters.
        i, j: Starting coordinates.
        fill: Character used to represent land in the output (default '*').
        blank: Character used to represent non-island cells (default ' ').

    Example:
        >>> g = [
        ...   ["1","1","0","0","0"],
        ...   ["1","1","0","0","0"],
        ...   ["0","0","1","0","0"],
        ...   ["0","0","0","1","1"]
        ... ]
        >>> print_island_at_dfs(g, 0, 0)
        **
        **
        <BLANKLINE>
        <BLANKLINE>
        >>> print_island_at_dfs(g, 2, 2)
        <BLANKLINE>
        <BLANKLINE>
          *
        <BLANKLINE>
        >>> print_island_at_dfs(g, 3, 3)
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
           **
        >>> print_island_at_dfs(g, 0, 2)
        Not on an island.
    """
    if not grid or not grid[0]:
        print("Empty grid.")
        return

    height = len(grid)
    width = len(grid[0])

    if not (0 <= i < height and 0 <= j < width):
        print("Out of bounds.")
        return
    if grid[i][j] != "1":
        print("Not on an island.")
        return

    visited = [[False for _ in range(width)] for _ in range(height)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    path = []  # store coordinates belonging to this island

    def dfs(x: int, y: int) -> None:
        # Base cases: out of bounds or not land / already visited
        if x < 0 or x >= height or y < 0 or y >= width:
            return
        if grid[x][y] == "0" or visited[x][y]:
            return

        visited[x][y] = True
        path.append((x, y))

        for i, j in directions:
            dx, dy = x + i, y + j
            dfs( dx, dy)

    # Collect this island only
    dfs(i, j)

    # Print full-size mask: fill for this island, blank elsewhere
    result = [[" " for _ in range(width)] for _ in range(height)]

    for x, y in path:
        result[x][y] = "*"

    for line in result:
        print("".join(line).rstrip())
