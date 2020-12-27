board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(current_board):
    print("Board: ")
    for row in range(len(current_board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(len(current_board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(current_board[row][col])
            else:
                print(str(current_board[row][col]) + " ", end="")


def find_empty_Space(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return row, col

def valid_board(board,number, position):
    # check rows
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # check cols
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True

def solve(board):
    find = find_empty_Space(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid_board(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    print_board(board)
    return False

solve(board)
