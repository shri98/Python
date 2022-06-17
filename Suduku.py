def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")

        print(end="\n")


def find_empty_location(arr, l):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True

    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[row + i][col + j] == num:
                return True
    return False


def is_position_secure(arr, row, col, num):
    return (not used_in_col(arr, col, num)) and (not used_in_row(arr, row, num)) and (
        not used_in_box(arr, row - row % 3, col - col % 3, num))


def solve_sudoku(arr):
    l = [0, 0]

    if not find_empty_location(arr, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):

        if is_position_secure(arr, row, col, num):
            arr[row][col] = num

            if solve_sudoku(arr):
                return True

        arr[row][col] = 0
    return False


grid = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 0, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 0, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 0, 4, 7, 2, 0, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 0, 8, 6, 3, 1, 0]
    ]

if (solve_sudoku(grid)):
    print_grid(grid)
else:
    print("no solution  exists ")

