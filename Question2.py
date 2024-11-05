C = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

B = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

def print_grid(C):
    for row in C:
        print(" ".join(map(str, row)))


def robot_coin_collection(Coin):
    n = len(Coin)      # Number of rows
    m = len(Coin[0])   # Number of columns

    F = [[0] * m for _ in range(n)]
    F[0][0] = Coin[0][0]

    for j in range(1, m):
        F[0][j] = F[0][j-1] + Coin[0][j]

    for i in range(1, n):
        F[i][0] = F[i-1][0] + Coin[i][0]
        for j in range(1, m):
            F[i][j] = max(F[i-1][j], F[i][j-1]) + Coin[i][j]
    print_grid(F)
    return F[n-1][m-1]

print("The maximum number of coins you collected is:",robot_coin_collection(C))
