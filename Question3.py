from Grid_info import grid1, grid2, grid3
from Grid_info import grid1_blockade, grid2_blockade, grid3_blockade

def print_grid(gridToPrint):
    """Prints grid in readable format."""
    for row in gridToPrint:
        print(" ".join(map(str, row)))

def robot_coin_collection(Coin, blockade):
    """Calculates maximum coins collectible in grid with blockades."""
    n = len(Coin)         # Number of rows in the grid
    m = len(Coin[0])      # Number of columns in the grid

    # Check if starting or ending point is blocked
    if blockade[0][0] == 'x' or blockade[n-1][m-1] == 'x':
        return "Starting or ending point is unreachable"

    # Populate F with zeros (Dynamic Programming table)
    F = [[0] * m for _ in range(n)]
    F[0][0] = Coin[0][0]   # Initialize starting cell with its coin value

    # Fill first column
    for i in range(1, n):
        if blockade[i][0] != 'x' and F[i-1][0] != "x":
            # If current cell is not blocked and the cell above is reachable
            F[i][0] = F[i-1][0] + Coin[i][0]   # Collect coins moving down
        else:
            F[i][0] = "x"   # Mark as unreachable due to blockade

    # Fill remaining grid
    for i in range(n):
        # Iterate through each column (starting from index 1)
        for j in range(1, m):
            # If current cell is not blocked
            if blockade[i][j] != 'x':
                if i > 0 and F[i-1][j] != "x" and F[i][j-1] != "x":
                    # Case 1: Can move from both above and left
                    F[i][j] = max(F[i-1][j], F[i][j-1]) + Coin[i][j]
                elif i > 0 and F[i-1][j] != "x":
                    # Case 2: Can only move from above
                    F[i][j] = F[i-1][j] + Coin[i][j]
                elif F[i][j-1] != "x":
                    # Case 3: Can only move from left
                    F[i][j] = F[i][j-1] + Coin[i][j]
                else:
                    # Case 4: No valid moves available
                    F[i][j] = "x"   # Mark as unreachable
            else:
                # If current cell is blocked
                F[i][j] = "x"

    # Check if the end point is reachable
    if F[n-1][m-1] == "x":
        return "End point is unreachable", F
    else:
        return F[n-1][m-1], F   # Return maximum coins collected and the DP table

if __name__ == "__main__":
    # Process grid1
    result1 = robot_coin_collection(grid1, grid1_blockade)
    if isinstance(result1, str):
        # If the end point is unreachable
        print(result1)
        _, max_coin_grid1 = result1
        print_grid(max_coin_grid1)
    else:
        max_coin1, max_coin_grid1 = result1
        print("The maximum number of coins you collected:", max_coin1)
        print_grid(max_coin_grid1)

    # Process grid2
    result2 = robot_coin_collection(grid2, grid2_blockade)
    if isinstance(result2, str):
        print(result2)
        _, max_coin_grid2 = result2
        print_grid(max_coin_grid2)
    else:
        max_coin2, max_coin_grid2 = result2
        print("The maximum number of coins you collected:", max_coin2)
        print_grid(max_coin_grid2)

    # Process grid3
    result3 = robot_coin_collection(grid3, grid3_blockade)
    if isinstance(result3, str):
        print(result3)
        _, max_coin_grid3 = result3
        print_grid(max_coin_grid3)
    else:
        max_coin3, max_coin_grid3 = result3
        print("The maximum number of coins you collected:", max_coin3)
        print_grid(max_coin_grid3)