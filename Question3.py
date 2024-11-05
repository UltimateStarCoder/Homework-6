from Grid_info import grid1, grid2, grid3
from Grid_info import grid1_blockade, grid2_blockade, grid3_blockade

def print_grid(gridToPrint):
    for row in gridToPrint:
        print(" ".join(map(str, row)))


def robot_coin_collection(Coin, blockade):
    n = len(Coin)      # Number of rows
    m = len(Coin[0])   # Number of columns

    if blockade[0][0] == 'x':
        return "Starting point is unreachable"

    # Populate F with 0 values for all cells to match the Coin grid size
    F = [[0] * m for _ in range(n)]
    F[0][0] = Coin[0][0]

    # Fill first column
    for i in range(1, n):
        if blockade[i-1][0] != 'x' and F[i-1][0] != "x":
            F[i][0] = F[i-1][0] + Coin[i][0]
        else:
            F[i][0] = "x"
        
        # Fill rest of the grid
        for j in range(1, m):
            if blockade[i][j] != 'x':
                if F[i-1][j] != "x" and F[i][j-1] != "x":
                    F[i][j] = max(F[i-1][j], F[i][j-1]) + Coin[i][j]
                elif F[i-1][j] != "x":
                    F[i][j] = F[i-1][j] + Coin[i][j]
                elif F[i][j-1] != "x":
                    F[i][j] = F[i][j-1] + Coin[i][j]
                else:
                    F[i][j] = "x"
            else:
                F[i][j] = "x"
    
    #print_grid(F)

    if F[n-1][m-1] == "x":
        return "End point is unreachable"
    else:
        return F[n-1][m-1], F
    
    
if __name__ == "__main__":
    max_coins, _ = robot_coin_collection(grid1, grid1_blockade)
    print("The maximum number of coins you collected is:", max_coins)

    max_coins2, _ = robot_coin_collection(grid2, grid2_blockade)
    print("The maximum number of coins you collected is:", max_coins2)

    max_coins3, _ = robot_coin_collection(grid3, grid3_blockade)
    print("The maximum number of coins you collected is:", max_coins3)
