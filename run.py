import os
import random


def clear_terminal():
    """
    Clears the terminal between actions to stop unnecessary scrolling
    """
    os.system('clear')


def title_art():
    """
    prints title ASCII art
    """
    print("████████████████████████████████████████████████████████████████████████████████")
    print("████   /          //    //    //   _   \  /    \\    _   \\             \   ████")
    print("███   /          //    //    //   //   / /  /\  \\   \\   \\             \   ███")
    print("██   /     _____//    //    //    '   / /  /  \  \\   \\   \\   \\   \\   \   ██")
    print("█   /          //     '    //    _   | /  /   /  / \   \\   \\   \\   \\   \   █")
    print("█  /______    //          //    //   //  /___/  /   \   `    \\   \\   \\   \  █")
    print("█ /          //__________//_________//_________/     \________\\___\\   \\   \ █")
    print("█/          /█ M   A   R   I   N   E ████ I   N   A   T   I   O   N █\   \\   \█")
    print("█__________/██████████████████████████████████████████████████████████\___\\___█")
    print("████████████████████████████████████████████████████████████████████████████████")


def full_block():
    """
    creates a full line of █
    """
    string = ""
    for i in range(0, 80):
        string = string + "█"
    return string


def player_win():
    """
    executes win message and option to restart the game
    """
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
    print("████████████████████████████████████████████████████████████████████████████")
    print("WE HAVE DOMINATED ALL ENEMY SUBS, COMMANDER")
    print("WE HAVE WON")

    query_new_game = str(input("NEW GAME? Y/N: ")).lower()
    while query_new_game not in "yn":
        print("COMMANDS ARE UNCLEAR COMMANDER, PLEASE ANSWER\n")
        query_new_game = str(input("NEW GAME? Y/N: ")).lower()
    if query_new_game == "y":
        main()
    else:
        title_menu()


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


def pick_coords(game_in_play):
    """
    Allows player to input coordinates
    """
    game_active = game_in_play
    dupe_stopper = False
    col_answer = False
    row_answer = False
    wrong_answer = False
    while dupe_stopper is False:
        while col_answer is False:
            try:
                if wrong_answer is True:
                    create_board()
                    print("COMMANDER, THESE ARE INVALID COORDINATES")
                    if game_active is True:
                        print("WE MUST TARGET A COLUMN ON THE RADAR\n")
                    else:
                        print("WE MUST POSITION OUR SUBS WITHIN VISIBLE COLUMNS\n")
                print("DESIGNATE RADAR COLUMN, COMMANDER")
                column_guess = str(input("pick a lettered column between A - H: ")).lower()
                if column_guess not in "abcdefgh" or column_guess.isdigit():
                    raise ValueError()
                elif len(column_guess) < 1:
                    raise ValueError()
                elif len(column_guess) > 1:
                    raise ValueError()
            except ValueError:
                wrong_answer = True
            else:
                col_answer = True
        wrong_answer = False
        column_guess_converted = ord(column_guess) - 96

        while row_answer is False:
            try:
                create_board()
                if wrong_answer is True:
                    print("COMMANDER, THESE ARE INVALID COORDINATES")
                    if game_active is True:
                        print(f"WE MUST STRIKE AN UN-TARGETED ROW IN COLUMN {column_guess.upper()}\n")
                    else:
                        print(f"WE MUST POSITION OUR SUB IN A ROW ON COLUMN {column_guess.upper()}\n")
                if game_active is True:
                    print(f"CALIBRATING TRAJECTORY TO COLUMN {column_guess.upper()}")
                    print("TRIANGULATE WITH RADAR ROW TO ESTBLISH TARGET BLAST ZONE\n")
                else:
                    print(f"TRIANGULATE RADAR COLUMN {column_guess.upper()} WITH RADAR ROWS TO POSITION SUB")
                row_guess = str(input("pick a numbered row between 1 - 5: "))
                if row_guess not in "12345":
                    raise ValueError()
                elif len(row_guess) < 1:
                    raise ValueError()
                elif len(row_guess) > 1:
                    raise ValueError()
            except ValueError:
                wrong_answer = True
            else:
                row_answer = True
                row_guess = int(row_guess)
        wrong_answer = False

        query_hit = hit_checker(row_guess, column_guess_converted, column_guess)
        if query_hit is False:
            dupe_stopper = True
        else:
            dupe_stopper = False
            col_answer = False
            row_answer = False
            wrong_answer = False
    return row_guess, column_guess_converted


def position_subs():
    """
    Allows player to position own subs at start of game
    """
    game_in_play = False
    for i in range(5):
        print(f"---POSITION SUB NUMBER  {i + 1}, COMMANDER---")
        row, col = pick_coords(game_in_play)

        while P_BOARD[row][col] == "@":
            create_board()
            print("COMMANDER, WE HAVE ALREADY DEPLOYED AT THESE COORDINATES")
            print("WE MUST EMPLOY TACTICAL MARINE ESPIONAGE")
            print(f"PLEASE RECONSIDER COORDINATES FOR SUB {i + 1}:\n")
            row, col = pick_coords(game_in_play)

        P_BOARD[row][col] = "@"
        create_board()
    return True


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


def comp_fire_torpedo():
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
        create_board()
    else:
        P_BOARD[c_row_guess][c_col_guess] = "."
        create_board()
    return [P_BOARD[c_row_guess][c_col_guess], c_col_converted, c_row_guess]


def fire_torpedo(enemy_positions, game_start):
    """
    chooses coordinates to strike
    """
    game_in_play = game_start
    print("COMMENCE ATTACK")
    row, col = pick_coords(game_in_play)
    print("col: ", col)
    print("row: ", row)
    for key in enemy_positions:
        if key == row:
            enemy_col = enemy_positions.get(key)
            if enemy_col == col:
                C_BOARD[row][col] = "X"
                # create_board()
                # enemy_hit(row, col)
            else:
                C_BOARD[row][col] = "."
                # create_board()
    return C_BOARD[row][col]


def create_board():
    """
    creates and displays the current state of
     the player board each time it is called
    """
    clear_terminal()
    b_perim = "                                          "
    b_wall = "███████████████████"
    print(full_block())
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
    print(f"{full_block()}\n")


def message_generator(player_target, comp_target):
    """
    generates messages depending on the outcome of the turn
    """
    create_board()
    if player_target in "X":
        print("\n----WE STRUCK THE ENEMY, COMMANDER.----\n")
    else:
        print("\n---NO ENEMY AT COORDINATES, COMMANDER.---\n")

    if comp_target[0] in "X":
        print(f"WE HAVE BEEN STRUCK COMMANDER! SUB {comp_target[1]}{comp_target[2]} HAS BEEN DOMINATED")
    else:
        print(f"WE HAVE OUTMANOEUVRED THE ENEMY'S STRIKE AT {comp_target[1]}{comp_target[2]} COMMANDER ")


def main():
    """
    main function that runs the whole game
    """
    # The game board ------------------------------------
    global P_BOARD
    global C_BOARD
    global COMP_SUBS

    P_BOARD = {
        1: ["1|", "~", "~", "~", "~", "~", "~", "~", "~"],
        2: ["2|", "~", "~", "~", "~", "~", "~", "~", "~"],
        3: ["3|", "~", "~", "~", "~", "~", "~", "~", "~"],
        4: ["4|", "~", "~", "~", "~", "~", "~", "~", "~"],
        5: ["5|", "~", "~", "~", "~", "~", "~", "~", "~"]
        }

    player_shipcount = 5

    C_BOARD = {
        1: ["|1", "~", "~", "~", "~", "~", "~", "~", "~"],
        2: ["|2", "~", "~", "~", "~", "~", "~", "~", "~"],
        3: ["|3", "~", "~", "~", "~", "~", "~", "~", "~"],
        4: ["|4", "~", "~", "~", "~", "~", "~", "~", "~"],
        5: ["|5", "~", "~", "~", "~", "~", "~", "~", "~"]
        }

    comp_shipcount = 5
    # The game board ------------------------------------
    create_board()
    COMP_SUBS = comp_position_subs()
    game_start = position_subs()

    while player_shipcount > 0 and comp_shipcount > 0:
        print(COMP_SUBS)
        player_turn = fire_torpedo(COMP_SUBS, game_start)
        comp_turn = comp_fire_torpedo()
        if player_turn == "X":
            comp_shipcount -= 1
        else:
            comp_shipcount -= 0

        if comp_turn[0] == "X":
            player_shipcount -= 1
        else:
            player_shipcount -= 0

        message_generator(player_turn, comp_turn)
        print(f"player lives remaining: {player_shipcount}")
        print(f"comp lives remaining: {comp_shipcount}")
    if comp_shipcount == 0:
        player_win()


def game_info_exp():
    """
    explains game rules and mechanics to user/player
    """
    b_perim = "                                          "
    b_wall = "███████████████████"
    print(full_block())
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{b_wall} +| A B C D E F G H || A B C D E F G H |+ {b_wall}")
    print(f"{b_wall} -|-----------------||-----------------|- {b_wall}")
    print(f"{b_wall} 1| ~ @ ~ ~ @ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |1 {b_wall}")
    print(f"{b_wall} 2| ~ ~ ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |2 {b_wall}")
    print(f"{b_wall} 3| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |3 {b_wall}")
    print(f"{b_wall} 4| ~ ~ ~ @ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |4 {b_wall}")
    print(f"{b_wall} 5| ~ ~ ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |5 {b_wall}")
    print(f"{b_wall} -|-----------------||-----------------|- {b_wall}")
    print(f"{b_wall} +| A B C D E F G H || A B C D E F G H |+ {b_wall}")
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{full_block()}")
    print("              WELCOME TO SUBMARINE DOMINATION SIMULATION COMMANDER")
    print("                   ABOVE IS AN EXAMPLE OF THE SIMULATED ARENA")
    print(f"{full_block()}")
    print("         AT THE START OF THE GAME, YOU WILL BE ASKED TO POSITION 5 SUBS")
    print("LIKE THIS:")
    print("        pick a lettered column between A - H:")
    print("THEN LIKE THIS")
    print("        pick a numbered row between 1 - 5:")
    print(f"{full_block()}")
    print('YOUR 5 SUBS WILL BE POSITIONED ON THE [LEFT] SIMULATED ARENA WITH "@"\n')
    print("THE HIGHLY ADVANCED AI WILL ALSO HIDE 5 SUBS ON THE [RIGHT] SIMULATED ARENA")
    print(f"{full_block()}")
    print("YOU AND THE HIGHLY ADVANCED AI WILL NOW TAKE TURNS")
    print("ATTEMPTING TO SINK EACH OTHER'S SUBS")
    print("SIMULATION WILL CONTINUE UNTIL YOU DOMINATE THE ENEMY")
    print("OR THE ENEMY DOMINATES YOU")
    print(f"{full_block()}")


def menu_option(title):
    """
    displays menu options and allows user to select a new game or instructions
    """
    title_option_select = False
    wrong_option_value = False
    while title_option_select is False:
        try:
            if wrong_option_value is True:
                if title is True:
                    clear_terminal()
                    title_art()
                else:
                    game_info_exp()
                print("INVALID CHOICE, PLEASE PICK FROM SPECIFIED OPTIONS:")
                print("+| N: New Game || I: How to Play || X: close simulation")
            else:
                print("+| N: New Game || I: How to Play || X: close simulation")

            option = str(input("pick a lettered option listed above: ")).lower()
            if option not in "nix" or option.isdigit():
                raise ValueError()
            elif len(option) < 1:
                raise ValueError()
            elif len(option) > 1:
                raise ValueError()
        except ValueError:
            wrong_option_value = True
        else:
            title_option_select = True
    wrong_option_value = False

    if option == "n":
        main()
    elif option == "i":
        game_info()
    else:
        print("closing simulation...")


def title_menu():
    """
    Title for the game with game starting options
    """
    clear_terminal()
    title_art()
    menu_option(True)


def game_info():
    """
    Game instructions with menu options
    """
    clear_terminal()
    game_info_exp()
    menu_option(False)


title_menu()
main()
