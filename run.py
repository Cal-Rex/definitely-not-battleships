import os
import random


def clear_terminal():
    """
    Clears the terminal between actions to stop unnecessary scrolling
    """
    os.system('clear')


def hit_checker(row, col, col_str):
    """
    Checks to see if a coordinate has been targeted before
    """
    if c_board[row][col] == "X":
        print(f"WE HAVE ALREADY NEUTRALIZED THREATS AT {col_str.upper()}{row}, COMMANDER")
        did_it_hit = True
    elif c_board[row][col] == ".":
        print(f"COORDINATES {col_str.upper()}{row} HAVE ALREADY BEEN STRUCK, COMMANDER")
        print("WE SHOULD CONSERVE OUR ORDINANCE, THINK OF THE BUDGET")
        did_it_hit = True
    else:
        did_it_hit = False
    return did_it_hit


def pick_coords():
    """
    Allows player to input coordinates
    """
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
    query_hit = hit_checker(row_guess, column_guess_converted, column_guess)
    if query_hit is True:
        fire_torpedo(comp_subs)
    else: 
        return row_guess, column_guess_converted


def position_subs():
    """
    Allows player to position own subs at start of game
    """
    for i in range(5):
        print(f"---POSITION SUB NUMBER  {i + 1}, COMMANDER---")
        row, col = pick_coords()
        p_board[row][col] = "@"
        clear_terminal()
        create_board()


def comp_position_subs():
    """
    assigns hidden coordinates for computer's subs
    """
    comp_coords = {}
    i = 0
    while i < 5:
        if i == 0:
            comp_coords[random.randint(1, 5)] = random.randint(1, 8)
            # print(f"first cycle ({i})")
            # print("comp_coords:", comp_coords)
            i += 1
        else:
            iterate_row = random.randint(1, 5)
            while iterate_row in comp_coords:
                iterate_row = random.randint(1, 5)
                # print("duplicate rolled, looping back round...")
            comp_coords[iterate_row] = random.randint(1, 8)
            # print("cycle:", i)
            # print("value rolled for row this turn:", iterate_row)
            # print("comp_coords:", comp_coords)
            i += 1
    # print(f"\nloop complete, final result: {comp_coords}\n")
    # print(f"exiting function...")
    return comp_coords


def enemy_hit(row, col):
    """
    upon successful hit, this function will reduce enemy lives
    """
    global COMP_SHIPCOUNT
    COMP_SHIPCOUNT = COMP_SHIPCOUNT - 1
    print("\n COMP_SHIPCOUNT is now: ", COMP_SHIPCOUNT)
    # print statement above here needs to be removed


def fire_torpedo(enemy_positions):
    """
    chooses coordinates to strike
    """
    print("COMMENCE ATTACK")
    print(enemy_positions)
    row, col = pick_coords()
    print("col: ", col)
    print("row: ", row)
    for key in enemy_positions:
        print("key is", key)
        if key == row:
            enemy_col = enemy_positions.get(key)
            if enemy_col == col:
                c_board[row][col] = "X"
                clear_terminal()
                create_board()
                print("\n----WE STRUCK THE ENEMY, COMMANDER.----\n")
                enemy_hit(row, col)
            else:
                c_board[row][col] = "."
                clear_terminal()
                create_board()
                print("\n---NO ENEMY AT COORDINATES, COMMANDER.---\n")    


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


# The game board ------------------------------------
p_board = {
    1: ["1|", "~", "~", "~", "~", "~", "~", "~", "~"],
    2: ["2|", "~", "~", "~", "~", "~", "~", "~", "~"],
    3: ["3|", "~", "~", "~", "~", "~", "~", "~", "~"],
    4: ["4|", "~", "~", "~", "~", "~", "~", "~", "~"],
    5: ["5|", "~", "~", "~", "~", "~", "~", "~", "~"]
    }

PLAYER_SHIPCOUNT = 5

c_board = {
    1: ["|1", "~", "~", "~", "~", "~", "~", "~", "~"],
    2: ["|2", "~", "~", "~", "~", "~", "~", "~", "~"],
    3: ["|3", "~", "~", "~", "~", "~", "~", "~", "~"],
    4: ["|4", "~", "~", "~", "~", "~", "~", "~", "~"],
    5: ["|5", "~", "~", "~", "~", "~", "~", "~", "~"]
    }

COMP_SHIPCOUNT = 5
# The game board ------------------------------------


create_board()
comp_subs = comp_position_subs()
print(comp_subs)
fire_torpedo(comp_subs)
fire_torpedo(comp_subs)
position_subs()
print(comp_subs)
fire_torpedo(comp_subs)