global N
N = 4


def print_board(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print(end="\n")


def is_safe(arr, row, col):
    for i in range(col):
        if arr[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1, ), range(col, -1, -1)):
        if arr[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if arr[i][j] == 1:
            return False

    return True


def solve_nqueens(arr, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(arr, i, col):

            arr[i][col] = 1

            if solve_nqueens(arr, col + 1):
                return True

            arr[i][col] = 0

    return False


if __name__ == "__main__":
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if not solve_nqueens(board, 0):
        print("Solution does not exist")
        print(False)

    print_board(board)
