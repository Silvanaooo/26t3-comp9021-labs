def f_1(*L) -> None:
    black_square = "⬛"
    white_square = "⬜"

    n = len(L)

    # Create an empty grid.
    grid = [[white_square for _ in range(2 * n + 1)]
            for _ in range(2 * n + 1)]

    # Repeat the first element to handle wrap-around.
    numbers = list(L) + [L[0]]

    # Generate the points of the closed polyline.
    points = []

    for i in range(0, len(numbers) - 2, 2):
        points.append((numbers[i], numbers[i + 1]))
        points.append((numbers[i + 2], numbers[i + 1]))

    points.append(points[0])

    # Convert (x, y) into (row, col).
    points = [(2 * y - 1, 2 * x - 1) for x, y in points]

    # Return all grid cells between two points.
    def collect_points(p1, p2):
        row1, col1 = p1
        row2, col2 = p2

        if row1 == row2:
            return [(row1, col)
                    for col in range(min(col1, col2), max(col1, col2) + 1)]

        if col1 == col2:
            return [(row, col1)
                    for row in range(min(row1, row2), max(row1, row2) + 1)]

    # Collect all cells belonging to the polyline.
    new_points = []

    for i in range(len(points) - 1):
        new_points.extend(collect_points(points[i], points[i + 1]))

    # Draw the polyline.
    for row, col in new_points:
        grid[row][col] = black_square

    # Print the grid.
    for row in grid:
        print("".join(row))