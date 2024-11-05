
def get_grid(rows, cols):
    coins = [(0, 3),(1, 3), (4,4)]
    # blocks = [(0, 1)]
    grid = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if (i, j) in coins:
                row.append(1)  # 1 for coins
            # elif (i, j) in blocks:
            #     row.append('x')  # x for blocks
            else:
                row.append(0)  # 0 for empty cells
        grid.append(row)
    
    return grid

# Example usage
grid = get_grid(6, 6)
for row in grid:
    print(' '.join(str(cell) for cell in row))