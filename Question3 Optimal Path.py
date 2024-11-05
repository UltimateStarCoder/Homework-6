from Grid_info import grid1, grid2, grid3
from Grid_info import grid1_blockade, grid2_blockade, grid3_blockade
from Question3 import robot_coin_collection, print_grid

    
def OptimalPath(Coin, blockade):
    _, F = robot_coin_collection(Coin, blockade)
    result = robot_coin_collection(Coin, blockade)
    if isinstance(result, str):
        return result

    n = len(Coin)      # Number of rows
    m = len(Coin[0])   # Number of columns

    # Populate F with 0 values for all cells to match the Coin grid size
    Optimus = [['.'] * m for _ in range(n)]

    # Trace back the path
    path = []
    i, j = n - 1, m - 1
    while i > 0 or j > 0:
        path.append((i, j))
        if i > 0 and j > 0:
            if F[i-1][j] != "x" and F[i][j-1] != "x":
                if F[i-1][j] > F[i][j-1]:
                    i -= 1  # Move up
                else:
                    j -= 1  # Move left
            elif F[i-1][j] != "x":
                i -= 1  # Move up
            elif F[i][j-1] != "x":
                j -= 1  # Move left
            else:
                break  # No valid path
        elif i > 0:
            if F[i-1][j] != "x":
                i -= 1  # Move up
            else:
                break  # No valid path
        elif j > 0:
            if F[i][j-1] != "x":
                j -= 1  # Move left
            else:
                break  # No valid path
    path.append((0, 0))  # Add the starting cell
    path.reverse()       # Reverse the path to start from (0, 0)
    # print(print_grid(path))

    # Mark the path with '*' in Optimus
    for i, j in path:
        Optimus[i][j] = '*'
    Optimus_grid = print_grid(Optimus)
    return Optimus_grid

_,result1 = robot_coin_collection(grid1, grid1_blockade)
print(print_grid(result1))
print(OptimalPath(grid1, grid1_blockade))

_,result2 = robot_coin_collection(grid2, grid2_blockade)
print(print_grid(result2))
print(OptimalPath(grid2, grid2_blockade))

