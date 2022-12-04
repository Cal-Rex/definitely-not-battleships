import os
import random


# to do: create game loss function

def clear_terminal():
    """
    Clears the terminal between actions to stop unnecessary scrolling
    """
    os.system('clear')


def title_art():
    """
    prints title ASCII art
    """
    print(r"████████████████████████████████████████████████████████████████████████████████")
    print(r"████   /          //    //    //   _   \  /    \\    _   \\             \   ████")
    print(r"███   /          //    //    //   //   / /  /\  \\   \\   \\             \   ███")
    print(r"██   /     _____//    //    //    '   / /  /  \  \\   \\   \\   \\   \\   \   ██")
    print(r"█   /          //     '    //    _   | /  /   /  / \   \\   \\   \\   \\   \   █")
    print(r"█  /______    //          //    //   //  /___/  /   \   `    \\   \\   \\   \  █")
    print(r"█ /          //__________//_________//_________/     \________\\___\\   \\   \ █")
    print(r"█/          /█ M   A   R   I   N   E ████ I   N   A   T   I   O   N █\   \\   \█")
    print(r"█__________/██████████████████████████████████████████████████████████\___\\___█")
    print(r"████████████████████████████████████████████████████████████████████████████████")


def full_block():
    """
    creates a full line of █
    """
    string = ""
    for i in range(0, 80):
        string = string + "█"
    return string


def player_lose():
    """
    executes loss message option to restart game
    """
    clear_terminal()
    print("                                ____")
    print("                        __,-~~/~    `---.")
    print("                      _/_,---(      ,    )")
    print("                  __ /        <    /   )  \___")
    print("     - ------===;;;'====------------------===;;;===----- -  -")
    print('                    \/  ~"~"~"~"~"~\~"~)~"/')
    print("                    (_ (   \  (     >    \)")
    print("                     \_( _ <         >_>'")
    print('                        ~ `-i` ::>|--"')
    print("                            I;|.|.|")
    print("      ,       ,       ,    <|i::|i|`.")
    print(r'   ./(     ./(     ./(   (` ^`"`-` ")   )`.     )`.     )`.')
    print("---'---`---'---`---'---`----------------'   `---'   `---'   `-----")
    query_new_game = str(input("NEW GAME? Y/N: ")).lower()
    while query_new_game not in "yn":
        print("                 COMMANDS ARE UNCLEAR COMMANDER, PLEASE ANSWER\n")
        query_new_game = str(input("          NEW GAME? Y/N: ")).lower()
    if query_new_game == "y":
        main()
    else:
        title_menu()


def player_win():
    """
    executes win message and option to restart the game
    """
    clear_terminal()

    print("                        +~'*^~ R E J O I C E ~^*'~+ \n")
    print(r"                                  |`-:_")
    print(r"         ,----....____            |    `+.")
    print(r"        (             ````----....|___   |")
    print(r"         \     _                      ````----....____")
    print(r"          \    _)                                     ```---.._")
    print(r"           \                                                   \ ")
    print(r"         )`.\  )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.")
    print(r"       -'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `")
    print(r"████████████████████████████████████████████████████████████████████████████")
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
        create_board()
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
                    print("                    COMMANDER, THESE ARE INVALID COORDINATES")
                    if game_active is True:
                        print("                      WE MUST TARGET A COLUMN ON THE RADAR\n")
                    else:
                        print("                WE MUST POSITION OUR SUBS WITHIN VISIBLE COLUMNS\n")
                print("                       DESIGNATE RADAR COLUMN, COMMANDER")
                column_guess = str(input(" pick a lettered column between A - H: ")).lower()
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
                    print("                    COMMANDER, THESE ARE INVALID COORDINATES")
                    if game_active is True:
                        print(f"                 WE MUST STRIKE AN UN-TARGETED ROW IN COLUMN {column_guess.upper()}\n")
                    else:
                        print(f"                 WE MUST POSITION OUR SUB IN A ROW ON COLUMN {column_guess.upper()}\n")
                if game_active is True:
                    print(f"                       CALIBRATING TRAJECTORY TO COLUMN {column_guess.upper()}")
                    print("            TRIANGULATE WITH RADAR ROW TO ESTBLISH TARGET BLAST ZONE\n")
                else:
                    print(f"           TRIANGULATE RADAR COLUMN {column_guess.upper()} WITH RADAR ROWS TO POSITION SUB")
                row_guess = str(input(" pick a numbered row between 1 - 5: "))
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
        print(f"                    ---POSITION SUB NUMBER  {i + 1}, COMMANDER---")
        row, col = pick_coords(game_in_play)
        PLAYER_SUBS.update({row: col})

        while P_BOARD[row][col] == "@":
            create_board()
            print("            COMMANDER, WE HAVE ALREADY DEPLOYED AT THESE COORDINATES")
            print("                    WE MUST EMPLOY TACTICAL MARINE ESPIONAGE")
            print(f"                    PLEASE RECONSIDER COORDINATES FOR SUB {i + 1}:\n")
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


def comp_fire_torpedo(turn_count, p_rows, p_columns):
    """
    function for comupters turn
    """
    if turn_count == 3:
        c_row_guess = p_rows[2]
        c_col_guess = p_columns[2]
    elif turn_count == 7:
        c_row_guess = p_rows[0]
        c_col_guess = p_columns[0]
    elif turn_count == 11:
        c_row_guess = p_rows[3]
        c_col_guess = p_columns[3]
    elif turn_count == 15:
        c_row_guess = p_rows[4]
        c_col_guess = p_columns[4]
    elif turn_count == 18:
        c_row_guess = p_rows[1]
        c_col_guess = p_columns[1]
    else:
        c_row_guess = random.randint(1, 5)
        c_col_guess = random.randint(1, 8)

    c_col_converted = chr(c_col_guess + 96).upper()
    while P_BOARD[c_row_guess][c_col_guess] == "X":
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
    print("                                COMMENCE ATTACK")
    row, col = pick_coords(game_in_play)
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
        print("                    ----WE STRUCK THE ENEMY, COMMANDER.----\n")
    else:
        print("                    ---NO ENEMY AT COORDINATES, COMMANDER.---\n")

    if comp_target[0] in "X":
        print(f"            WE HAVE BEEN STRUCK COMMANDER! SUB {comp_target[1]}{comp_target[2]} HAS BEEN DOMINATED")
    else:
        print(f"            WE HAVE OUTMANOEUVRED THE ENEMY'S STRIKE AT {comp_target[1]}{comp_target[2]} COMMANDER")


def main():
    """
    main function that runs the whole game
    """
    global P_BOARD
    global C_BOARD
    global COMP_SUBS
    global PLAYER_SUBS

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

    turns = 0
    create_board()

    COMP_SUBS = comp_position_subs()
    
    PLAYER_SUBS = {}
    p_rows = []
    p_columns = []
    game_start = position_subs()
    for key, value in PLAYER_SUBS.items():
        p_rows.append(key)
        p_columns.append(value)

    while player_shipcount > 0 and comp_shipcount > 0:
        print(COMP_SUBS)
        player_turn = fire_torpedo(COMP_SUBS, game_start)
        comp_turn = comp_fire_torpedo(turns, p_rows, p_columns)
        if player_turn == "X":
            comp_shipcount -= 1
        else:
            comp_shipcount -= 0

        if comp_turn[0] == "X":
            player_shipcount -= 1
        else:
            player_shipcount -= 0

        message_generator(player_turn, comp_turn)
        print(f"             COMMANDER SUBS REMAINING : {player_shipcount}     ||     {comp_shipcount} : AI SUBS REMAINING")
        turns += 1
    if comp_shipcount == 0:
        player_win()
    elif player_shipcount == 0:
        player_lose()


def game_info_exp():
    """
    explains game rules and mechanics to user/player
    """
    b_perim = "                                          "
    b_wall = "█                 █"
    print(full_block())
    print(f"{b_wall}{b_perim}{b_wall}")
    print(r"█   WELCOME TO    █ +| A B C D E F G H || A B C D E F G H |+ █        THIS IS  █")
    print(r"█   SUBMARINE     █ -|-----------------||-----------------|- █  AN EXAMPLE OF  █")
    print(r"█   DOMINATION    █ 1| ~ @ ~ ~ @ ~ ~ ~ || ~ ~ X ~ ~ ~ ~ ~ |1 █  THE SIMULATED  █")
    print(r"█   SIMULATION    █ 2| ~ ~ ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |2 █          ARENA  █")
    print(f"█   COMMANDER     █ 3| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ . ~ ~ ~ |3 {b_wall}")
    print(f"{b_wall} 4| ~ ~ ~ X ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |4 █    ENEMY SUBS   █")
    print(r"█ [LEFT] IS YOUR  █ 5| ~ . ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |5 █ARE HIDDEN[RIGHT]█")
    print(r"█      ZONE       █ -|-----------------||-----------------|- █ . = MISSED SHOT █")
    print(r"█ @ = YOUR SHIPS  █ +| A B C D E F G H || A B C D E F G H |+ █  X = SUNK SUB   █")
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{full_block()}")
    print("         AT THE START OF THE GAME, YOU WILL BE ASKED TO POSITION 5 SUBS")
    print("              LIKE THIS:")
    print("                     pick a lettered column between A - H:")
    print("              THEN LIKE THIS:")
    print("                      pick a numbered row between 1 - 5:")
    print(f"{full_block()}")
    print("      YOU WILL THEN USE THIS SAME PROCESS TO PREDICT ENEMY SUB PLACEMENT")
    print("    THE HIGHLY ADVANCED AI WILL IN-TURN ATTEMPT TO PREDICT YOUR HIDDEN SUBS")
    print("          SIMULATION STEPS REPEAT UNTIL ALL 5 ENEMY SUBS ARE DOMINATED")
    print("                      OR ENEMY DOMINATES ALL 5 OF YOUR SUBS")


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
                    clear_terminal()
                    game_info_exp()
                print("           +| N: New Game || I: How to Play || X: close simulation |+")
                print("               INVALID CHOICE, PLEASE PICK FROM SPECIFIED OPTIONS\n")
            else:
                print("           +| N: New Game || I: How to Play || X: close simulation |+\n")

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
