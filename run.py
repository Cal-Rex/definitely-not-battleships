def pick_coords():
    column_guess = str(input("pick a lettered column between A - H: ")).lower()
    while column_guess not in "abcdefgh" or column_guess.isdigit():
        print("you entered bad coords captain, try again!\n")
        column_guess = str(input("pick a lettered column between A - H: ")).lower()

    print(column_guess)
    column_guess_converted = ord(column_guess) - 96
    print(f"\nYou Selected: {column_guess_converted}\n")

    row_guess = input("pick a numbered row between 1 - 5: ")
    while row_guess not in "12345":
        print("you entered bad coords captain, try again!\n")
        row_guess = input("pick a numbered row between 1 - 5: ")

    row_guess = int(row_guess)
    print(f"\nYou selected {row_guess}\n")
    # 2 values used to target specific key:value pairs
    return column_guess_converted, row_guess


def fire_torpedo():
    """
    chooses coordinates to strike
    """
    col, row = pick_coords()
    c_board[col][row] = "."

    create_board()


p_board = {
    1: ["1|", "~", "~", "~", "~", "~", "~", "~", "~"],
    2: ["2|", "~", "~", "~", "~", "~", "~", "~", "~"],
    3: ["3|", "~", "~", "~", "~", "~", "~", "~", "~"],
    4: ["4|", "~", "~", "~", "~", "~", "~", "~", "~"],
    5: ["5|", "~", "~", "~", "~", "~", "~", "~", "~"]
    }

c_board = {
    1: ["|1", "~", "~", "~", "~", "~", "~", "~", "~"],
    2: ["|2", "~", "~", "~", "~", "~", "~", "~", "~"],
    3: ["|3", "~", "~", "~", "~", "~", "~", "~", "~"],
    4: ["|4", "~", "~", "~", "~", "~", "~", "~", "~"],
    5: ["|5", "~", "~", "~", "~", "~", "~", "~", "~"]
    }


def create_board():
    print("+| A B C D E F G H | A B C D E F G H |+")
    print("-|-----------------|-----------------|-")
    print(" ".join(p_board[1]), "|", " ".join(c_board[1][1:]), c_board[1][0])
    print(" ".join(p_board[2]), "|", " ".join(c_board[2][1:]), c_board[2][0])
    print(" ".join(p_board[3]), "|", " ".join(c_board[3][1:]), c_board[3][0])
    print(" ".join(p_board[4]), "|", " ".join(c_board[4][1:]), c_board[4][0])
    print(" ".join(p_board[5]), "|", " ".join(c_board[5][1:]), c_board[5][0])
    print("-|-----------------|-----------------|-")
    print("+| A B C D E F G H | A B C D E F G H |+\n")


create_board()
fire_torpedo()
