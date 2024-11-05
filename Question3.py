from Grid_info import grid1, grid2, grid3
from Grid_info import grid1_blockade, grid2_blockade, grid3_blockade

def print_grid(gridToPrint):
    """Prints grid in readable format."""
    for row in gridToPrint:
        print(" ".join(map(str, row)))

def robot_coin_collection(Coin, blockade):
    """Calculates maximum coins collectible in grid with blockades."""
    n = len(Coin)
    m = len(Coin[0])

    if blockade[0][0] == 'x' or blockade[n-1][m-1] == 'x':
        return "Starting or ending point is unreachable"

    # Populate F with zeros
    F = [[0] * m for _ in range(n)]
    F[0][0] = Coin[0][0]

    # Fill first column
    for i in range(1, n):
        if blockade[i-1][0] != 'x' and F[i-1][0] != "x":
            F[i][0] = F[i-1][0] + Coin[i][0]
        else:
            F[i][0] = "x"

    # Fill rest of grid
    for i in range(n):
        for j in range(1, m):
            if blockade[i][j] != 'x':
                if i > 0 and F[i-1][j] != "x" and F[i][j-1] != "x":
                    F[i][j] = max(F[i-1][j], F[i][j-1]) + Coin[i][j]
                elif i > 0 and F[i-1][j] != "x":
                    F[i][j] = F[i-1][j] + Coin[i][j]
                elif F[i][j-1] != "x":
                    F[i][j] = F[i][j-1] + Coin[i][j]
                else:
                    F[i][j] = "x"
            else:
                F[i][j] = "x"

    if F[n-1][m-1] == "x":
        return "End point is unreachable", F
    else:
        return F[n-1][m-1], F

if __name__ == "__main__":
    result1 = robot_coin_collection(grid1, grid1_blockade)
    if isinstance(result1, str):
        print(result1)
        _, max_coin_grid1 = result1
        print_grid(max_coin_grid1)
    else:
        max_coin1, max_coin_grid1 = result1
        print("The maximum number of coins you collected:", max_coin1)
        print_grid(max_coin_grid1)

    result2 = robot_coin_collection(grid2, grid2_blockade)
    if isinstance(result2, str):
        print(result2)
        _, max_coin_grid2 = result2
        print_grid(max_coin_grid2)
    else:
        max_coin2, max_coin_grid2 = result2
        print("The maximum number of coins you collected:", max_coin2)
        print_grid(max_coin_grid2)

    result3 = robot_coin_collection(grid3, grid3_blockade)
    if isinstance(result3, str):
        print(result3)
        _, max_coin_grid3 = result3
        print_grid(max_coin_grid3)
    else:
        max_coin3, max_coin_grid3 = result3
        print("The maximum number of coins you collected:", max_coin3)
        print_grid(max_coin_grid3)