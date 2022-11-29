import os
import random


# notes:
# 1. game will throw error and break if no value is given on an input
# 2. when comp strikes subs, P_BOARD variable is not updated
# 3. if error message created in while loop, correct row value after entering column will throw

# steps needed to complete:
# 2. create functions that allows computer to take shots
# 3. create losing criteria if player lives drop to 0

def clear_terminal():
    """
    Clears the terminal between actions to stop unnecessary scrolling
    """
    os.system('clear')


def player_win():
    """
    executes win message and option to restart the game
    """
    global GAME_ACTIVE
    GAME_ACTIVE = False

    clear_terminal()

    print("                        +~'*^~ R E J O I C E ~^*'~+ \n")
    print("                                  |`-:_")
    print("         ,----....____            |    `+.")
    print("        (             ````----....|___   |")
    print("         \     _                      ````----....____")
    print("          \    _)                                     ```---.._")
    print("           \                                                   \ ")
    print("         )`.\  )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.")
    print("       -'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `")
    print("WE HAVE DOMINATED ALL ENEMY SUBS, COMMANDER")
    print("WE HAVE WON")

    query_new_game = str(input("NEW GAME? Y/N: ")).lower()
    while query_new_game not in "yn":
        print("COMMANDS ARE UNCLEAR COMMANDER, PLEASE ANSWER\n")
        query_new_game = str(input("NEW GAME? Y/N: ")).lower()
    if query_new_game == "y":
        main()
    else:
        title()


def hit_checker(row, col, col_str):
    """
    Checks to see if a coordinate has been targeted before
    """
    if C_BOARD[row][col] == "X":
        print(f"WE HAVE ALREADY NEUTRALIZED THREATS AT {col_str.upper()}{row}, COMMANDER")
        did_it_hit = True
    elif C_BOARD[row][col] == ".":
        print(f"COORDINATES {col_str.upper()}{row} HAVE ALREADY BEEN STRUCK, COMMANDER")
        print("WE SHOULD CONSERVE OUR ORDINANCE, THINK OF THE BUDGET\n")
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
    query_hit = hit_checker(row_guess, column_guess_converted, column_guess)
    if query_hit is True:
        fire_torpedo(COMP_SUBS)
    else:
        return row_guess, column_guess_converted


def position_subs():
    """
    Allows player to position own subs at start of game
    """
    for i in range(5):
        print(f"---POSITION SUB NUMBER  {i + 1}, COMMANDER---")
        row, col = pick_coords()

        while P_BOARD[row][col] == "@":
            clear_terminal()
            create_board()
            print("COMMANDER, WE HAVE ALREADY DEPLOYED AT THESE COORDINATES")
            print("WE MUST EMPLOY TACTICAL MARINE ESPIONAGE")
            print(f"PLEASE RECONSIDER COORDINATES FOR SUB {i + 1}:\n")
            row, col = pick_coords()

        P_BOARD[row][col] = "@"

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
            i += 1
        else:
            iterate_row = random.randint(1, 5)
            while iterate_row in comp_coords:
                iterate_row = random.randint(1, 5)
            comp_coords[iterate_row] = random.randint(1, 8)
            i += 1
    return comp_coords


def comp_turn():
    """
    function for comupters turn
    """
    c_row_guess = random.randint(1, 5)
    c_col_guess = random.randint(1, 8)
    c_col_converted = chr(c_col_guess + 96).upper()
    while P_BOARD[c_row_guess][c_col_guess] == "X":
        print(f"rolled {c_col_converted}{c_row_guess} comp had to re-roll")
        c_row_guess = random.randint(1, 5)
        c_col_guess = random.randint(1, 8)
    if P_BOARD[c_row_guess][c_col_guess] == "@":
        P_BOARD[c_row_guess][c_col_guess] = "X"
        print(f"WE HAVE BEEN STRUCK COMMANDER! SUB {c_col_converted}{c_row_guess} IS DOWNED")
        
    else:
        P_BOARD[c_row_guess][c_col_guess] = "."
        print(f"WE HAVE OUTMANOEUVRED THE ENEMY'S STRIKE AT {c_col_converted}{c_row_guess} COMMANDER ")


def enemy_hit(row, col):
    """
    upon successful hit, this function will reduce enemy lives
    """
    global COMP_SHIPCOUNT
    COMP_SHIPCOUNT = COMP_SHIPCOUNT - 1
    print("\n----WE STRUCK THE ENEMY, COMMANDER.----\n")


def fire_torpedo(enemy_positions):
    """
    chooses coordinates to strike
    """
    if GAME_ACTIVE is True:
        print("COMMENCE ATTACK")
        print(enemy_positions)
        row, col = pick_coords()
        print("col: ", col)
        print("row: ", row)
        for key in enemy_positions:
            if key == row:
                enemy_col = enemy_positions.get(key)
                if enemy_col == col:
                    C_BOARD[row][col] = "X"
                    clear_terminal()
                    create_board()
                    enemy_hit(row, col)
                else:
                    C_BOARD[row][col] = "."
                    clear_terminal()
                    create_board()
                    print("\n---NO ENEMY AT COORDINATES, COMMANDER.---\n") 


def create_board():
    """
    creates and displays the current state of
     the player board each time it is called
    """
    b_edge = "████████████████████████████████████████████████████████████████████████████████"
    b_perim = "                                          "
    b_wall = "███████████████████"
    print(b_edge)
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{b_wall} +| A B C D E F G H || A B C D E F G H |+ {b_wall}")
    print(f"{b_wall} -|-----------------||-----------------|- {b_wall}")
    print(b_wall, " ".join(P_BOARD[1]), "||", " ".join(C_BOARD[1][1:]), C_BOARD[1][0], b_wall)
    print(b_wall, " ".join(P_BOARD[2]), "||", " ".join(C_BOARD[2][1:]), C_BOARD[2][0], b_wall)
    print(b_wall, " ".join(P_BOARD[3]), "||", " ".join(C_BOARD[3][1:]), C_BOARD[3][0], b_wall)
    print(b_wall, " ".join(P_BOARD[4]), "||", " ".join(C_BOARD[4][1:]), C_BOARD[4][0], b_wall)
    print(b_wall, " ".join(P_BOARD[5]), "||", " ".join(C_BOARD[5][1:]), C_BOARD[5][0], b_wall)
    print(f"{b_wall} -|-----------------||-----------------|- {b_wall}")
    print(f"{b_wall} +| A B C D E F G H || A B C D E F G H |+ {b_wall}")
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{b_edge}\n")


def main():
    """
    main function that runs the whole game
    """
    # The game board ------------------------------------
    global P_BOARD
    global C_BOARD
    global PLAYER_SHIPCOUNT
    global COMP_SHIPCOUNT
    global COMP_SUBS
    global GAME_ACTIVE

    P_BOARD = {
        1: ["1|", "~", "~", "~", "~", "~", "~", "~", "~"],
        2: ["2|", "~", "~", "~", "~", "~", "~", "~", "~"],
        3: ["3|", "~", "~", "~", "~", "~", "~", "~", "~"],
        4: ["4|", "~", "~", "~", "~", "~", "~", "~", "~"],
        5: ["5|", "~", "~", "~", "~", "~", "~", "~", "~"]
        }

    PLAYER_SHIPCOUNT = 5

    C_BOARD = {
        1: ["|1", "~", "~", "~", "~", "~", "~", "~", "~"],
        2: ["|2", "~", "~", "~", "~", "~", "~", "~", "~"],
        3: ["|3", "~", "~", "~", "~", "~", "~", "~", "~"],
        4: ["|4", "~", "~", "~", "~", "~", "~", "~", "~"],
        5: ["|5", "~", "~", "~", "~", "~", "~", "~", "~"]
        }

    COMP_SHIPCOUNT = 5
    # The game board ------------------------------------

    GAME_ACTIVE = True
    create_board()
    COMP_SUBS = comp_position_subs()
    
    position_subs()
    while PLAYER_SHIPCOUNT > 0 and COMP_SHIPCOUNT > 0:
        print(COMP_SUBS)
        fire_torpedo(COMP_SUBS)
        comp_turn()
    if COMP_SHIPCOUNT == 0:
        player_win()


def title():
    """
    Title for the game with game starting options
    """
    clear_terminal()
    print("████████████████████████████████████████████████████████████████████████████████")
    print("████    /          //    //    //   _   \  /   _  \   /   _    //      \    ████")
    print("███    /          //    //    //   //   / /   / \  \ /   //   //        \    ███")
    print("██    /    ______//    //    //    `   / /   /  /  //   //   //          \    ██")
    print("█    /          //     `    //    _   | /   /  /  //   //   //   |   |    \    █")
    print("█   /______    //          //    //   //    ```  //    `   //    |   |     \   █")
    print("█  /          //__________//_________//_________//________//_____|___|      \  █")
    print("█ /          /█ M   A   R   I   N   E ███ I   N   A   T   I   O   N █|       \ █")
    print("█/__________/ ███████████████████████████████████████████████████████|________\█")
    print("████████████████████████████████████████████████████████████████████████████████")


main()
title()