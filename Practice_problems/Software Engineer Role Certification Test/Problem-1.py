def count_max_cells(upRight):
  """Counts the number of cells containing the maximum value in an infinite two-dimensional grid filled with zeros, indexed from (1, 1) at the bottom left corner with coordinates increasing toward the top and right.

  Args:
    upRight: A list of space-separated integers, where each pair of integers represents a coordinate (r, c) in the grid.

  Returns:
    The number of cells containing the maximum value in the grid.
  """

  # Initialize variables
  max_value = 0
  max_count = 0

  # Initialize the grid with zeros
  grid = [[0 for _ in range(10000)] for _ in range(10000)]

  # Iterate through each coordinate in the upRight array
  for coordinate in upRight:
    r, c = map(int, coordinate.split())

    # Increment all cells from (1, 1) to (r, c) by 1
    for i in range(1, r + 1):
      for j in range(1, c + 1):
        grid[i][j] += 1

    # Update max_value if the newly added value is greater than the current max_value
    max_value = max(max_value, grid[r][c])

  # Iterate through each cell in the grid
  for i in range(1, 10000):
    for j in range(1, 10000):
      # If the cell's value is equal to max_value, increment max_count
      if grid[i][j] == max_value:
        max_count += 1

  return max_count