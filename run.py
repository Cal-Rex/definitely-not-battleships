import os
import random


# to do: create game loss function

def clear_terminal():
    """
    Clears the terminal between actions to stop unnecessary scrolling
    """
    os.system('clear')


def full_block():
    """
    creates a full line of █
    """
    string = ""
    for i in range(0, 80):
        string = string + "█"
    return string


def title_art():
    """
    prints title ASCII art
    """
    line_1a = r"████   /          //    //    //   _   \ "
    line_1b = r" /    \\    _   \\             \   ████"
    line_2a = r"███   /          //    //    //   //   / "
    line_2b = r"/  /\  \\   \\   \\             \   ███"
    line_3a = r"██   /     _____//    //    //    '   / /"
    line_3b = r"  /  \  \\   \\   \\   \\   \\   \   ██"
    line_4a = r"█   /          //     '    //    _   | /"
    line_4b = r"  /   /  / \   \\   \\   \\   \\   \   █"
    line_5a = r"█  /______    //          //    //   //"
    line_5b = r"  /___/  /   \   `    \\   \\   \\   \  █"
    line_6a = r"█ /          //__________//_________//_"
    line_6b = r"________/     \________\\___\\   \\   \ █"
    line_7a = r"█/          /█ M   A   R   I   N   E ██"
    line_7b = r"██ I   N   A   T   I   O   N █\   \\   \█"
    line_8a = r"█__________/███████████████████████████"
    line_8b = r"███████████████████████████████\___\\___█"

    print(full_block())
    print(f"{line_1a}{line_1b}")
    print(f"{line_2a}{line_2b}")
    print(f"{line_3a}{line_3b}")
    print(f"{line_4a}{line_4b}")
    print(f"{line_5a}{line_5b}")
    print(f"{line_6a}{line_6b}")
    print(f"{line_7a}{line_7b}")
    print(f"{line_8a}{line_8b}")
    print(full_block())


def player_lose():
    """
    executes loss message option to restart game
    """
    exp_1 = r"                                ____"
    exp_2 = r"                        __,-~~/~    `---."
    exp_3 = r"                      _/_,---(      ,    )"
    exp_4 = r"                  __ /        <    /   )  \___"
    exp_5 = r"    - ------===;;;'====------------------===;;;===----- -  -"
    exp_6 = r'                    \/  ~"~"~"~"~"~\~"~)~"/'
    exp_7 = r"                    (_ (   \  (     >    \)"
    exp_8 = r"                     \_( _ <         >_>'"
    exp_9 = r'                        ~ `-i` ::>|--"'
    exp_10 = r"                            I;|.|.|"
    exp_11 = r"      ,       ,       ,    <|i::|i|`."
    exp_12 = r'    ./(     ./(     ./(   (` ^`"`-` ")   )`.     )`.     )`.'
    exp_13a = r"---'---`---'---`---'---`-------"
    exp_13b = r"---------'   `---'   `---'   `-----"
    space = r"                 "
    msg_1a = r"         THE ENEMY DOMINATED ALL OF OUR"
    msg_1b = r" SUBS COMMANDER. WE HAVE LOST"
    error_msg1 = r"                 COMMANDS ARE UNCLEAR"
    error_msg2 = " COMMANDER, PLEASE ANSWER\n"
    clear_terminal()
    print(f"{space}{exp_1}")
    print(f"{space}{exp_2}")
    print(f"{space}{exp_3}")
    print(f"{space}{exp_4}")
    print(f"{space}{exp_5}")
    print(f"{space}{exp_6}")
    print(f"{space}{exp_7}")
    print(f"{space}{exp_8}")
    print(f"{space}{exp_9}")
    print(f"{space}{exp_10}")
    print(f"{space}{exp_11}")
    print(f"{space}{exp_12}")
    print(f"{space}{exp_13a}{exp_13b}")
    print(full_block())
    print(f"{msg_1a}{msg_1b}")
    query_new_game = str(input("          NEW GAME? Y/N: ")).lower()
    while query_new_game not in "yn":
        print(f"{error_msg1}{error_msg2}")
        query_new_game = str(input("          NEW GAME? Y/N: ")).lower()
    if query_new_game == "y":
        main()
    else:
        title_menu()


def player_win():
    """
    executes win message and option to restart the game
    """
    sub_1 = "                        +~'*^~ R E J O I C E ~^*'~+ \n"
    sub_2 = r"                                  |`-:_"
    sub_3 = r"         ,----....____            |    `+."
    sub_4 = r"        (             ````----....|___   |"
    sub_5 = r"         \     _                      ````----....____"
    sub_6 = r"          \    _)                                     ```---.._"
    sub_7a = r"           \                   "
    sub_7b = r"                                \ "
    sub_8a = r"         )`.\  )`.   )`.   )`.   )`.  "
    sub_8b = r" )`.   )`.   )`.   )`.   )`.   )`."
    sub_9a = r"       -'   `-'   `-'   `-'   `-"
    sub_9b = r"'   `-'   `-'   `-'   `-'   `-'   `-'   `"
    space = r"   "

    clear_terminal()
    print(space + sub_1)
    print(space + sub_2)
    print(space + sub_3)
    print(space + sub_4)
    print(space + sub_5)
    print(space + sub_6)
    print(space + sub_7a + sub_7b)
    print(space + sub_8a + sub_8b)
    print(space + sub_9a + sub_9b)
    print(full_block())

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
    err_msg_1a = "WE HAVE ALREADY NEUTRALIZED THREATS AT"
    err_msg_1b = f" {col_str.upper()}{row}, COMMANDER"
    err_msg_2a = f"COORDINATES {col_str.upper()}{row} "
    err_msg_2b = "HAVE ALREADY BEEN STRUCK, COMMANDER"

    if C_BOARD[row][col] == "X":
        print(f"{err_msg_1a}{err_msg_1b}")
        did_it_hit = True
    elif C_BOARD[row][col] == ".":
        create_board()
        print(f"{err_msg_2a}{err_msg_2b}")
        print("WE SHOULD CONSERVE OUR ORDINANCE, THINK OF THE BUDGET\n")
        did_it_hit = True
    else:
        did_it_hit = False

    return did_it_hit


def pick_coords(game_in_play):
    """
    Allows player to input coordinates
    """
    c_wa_print_1 = "                    COMMANDER,"
    c_wa_print_2 = " THESE ARE INVALID COORDINATES"

    cga_print_1a = "                      WE "
    cga_print_1b = "MUST TARGET A COLUMN ON THE RADAR\n"
    cga_print_2a = "                WE MUST POSITION"
    cga_print_2b = " OUR SUBS WITHIN VISIBLE COLUMNS\n"
    cga_print_3a = "                       "
    cga_print_3b = "DESIGNATE RADAR COLUMN, COMMANDER"

    cg_str = " pick a lettered column between A - H: "

    r_wa_print_1 = "                    COMMANDER, "
    r_wa_print_2 = "THESE ARE INVALID COORDINATES"

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
                    print(f"{c_wa_print_1}{c_wa_print_2}")
                    if game_active is True:
                        print(f"{cga_print_1a}{cga_print_1b}")
                    else:
                        print(f"{cga_print_2a}{cga_print_2b}")
                print(f"{cga_print_3a}{cga_print_3b}")
                column_guess = str(input(f"{cg_str}")).lower()
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
        rga_print_1a = "                 WE MUST STRIKE AN UN-TARGETED"
        rga_print_1b = f" ROW IN COLUMN {column_guess.upper()}\n"
        rga_print_2a = "                 WE MUST POSITION OUR SUB IN "
        rga_print_2b = f"A ROW ON COLUMN {column_guess.upper()}\n"
        rga_print_3a = "                       CALIBRATING TRAJECTORY "
        rga_print_3b = f"TO COLUMN {column_guess.upper()}"
        rga_print_3c = "            TRIANGULATE WITH RADAR ROW "
        rga_print_3d = "TO ESTBLISH TARGET BLAST ZONE\n"
        rga_print_4a = "           TRIANGULATE RADAR COLUMN "
        rga_print_4b = f"{column_guess.upper()} WITH RADAR"
        rga_print_4c = "ROWS TO POSITION SUB"

        while row_answer is False:
            try:
                create_board()
                if wrong_answer is True:
                    print(f"{r_wa_print_1}{r_wa_print_2}")
                    if game_active is True:
                        print(f"{rga_print_1a}{rga_print_1b}")
                    else:
                        print(f"{rga_print_2a}{rga_print_2b}")
                if game_active is True:
                    print(f"{rga_print_3a}{rga_print_3b}")
                    print(f"{rga_print_3c}{rga_print_3d}")
                else:
                    print(f"{rga_print_4a}{rga_print_4b}{rga_print_4c}")
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

        hit = hit_checker(row_guess, column_guess_converted, column_guess)
        if hit is False:
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
    loop_1_txt = "                    ---POSITION SUB NUMBER  "
    loop_2_txta = "            COMMANDER, WE HAVE ALREADY"
    loop_2_txtb = " DEPLOYED AT THESE COORDINATES"
    loop_2_txtc = "                    WE MUST EMPLOY"
    loop_2_txtd = " TACTICAL MARINE ESPIONAGE"
    loop_2_txte = "                    PLEASE RECONSIDER "
    game_in_play = False
    for i in range(5):
        print(f"{loop_1_txt}{i + 1}, COMMANDER---")
        row, col = pick_coords(game_in_play)
        PLAYER_SUBS.update({row: col})

        while P_BOARD[row][col] == "@":
            create_board()
            print(f"{loop_2_txta}{loop_2_txtb}")
            print(f"{loop_2_txtc}{loop_2_txtd}")
            print(f"{loop_2_txte}COORDINATES FOR SUB {i + 1}:\n")
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
            else:
                C_BOARD[row][col] = "."

    return C_BOARD[row][col]


def create_board():
    """
    creates and displays the current state of
     the player board each time it is called
    """
    b_perim = "                                          "
    b_wall = "███████████████████"
    concat_pboard_1 = f'{b_wall} {" ".join(P_BOARD[1])} ||'
    concat_pboard_2 = f'{b_wall} {" ".join(P_BOARD[2])} ||' 
    concat_pboard_3 = f'{b_wall} {" ".join(P_BOARD[3])} ||'
    concat_pboard_4 = f'{b_wall} {" ".join(P_BOARD[4])} ||'
    concat_pboard_5 = f'{b_wall} {" ".join(P_BOARD[5])} ||'

    concat_cboard_1 = f'{" ".join(C_BOARD[1][1:])} {C_BOARD[1][0]} {b_wall}'
    concat_cboard_2 = f'{" ".join(C_BOARD[2][1:])} {C_BOARD[2][0]} {b_wall}'
    concat_cboard_3 = f'{" ".join(C_BOARD[3][1:])} {C_BOARD[3][0]} {b_wall}'
    concat_cboard_4 = f'{" ".join(C_BOARD[4][1:])} {C_BOARD[4][0]} {b_wall}'
    concat_cboard_5 = f'{" ".join(C_BOARD[5][1:])} {C_BOARD[5][0]} {b_wall}'
    clear_terminal()

    print(full_block())
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{b_wall} +| A B C D E F G H || A B C D E F G H |+ {b_wall}")
    print(f"{b_wall} -|-----------------||-----------------|- {b_wall}")
    print(concat_pboard_1, concat_cboard_1)
    print(concat_pboard_2, concat_cboard_2)
    print(concat_pboard_3, concat_cboard_3)
    print(concat_pboard_4, concat_cboard_4)
    print(concat_pboard_5, concat_cboard_5)
    print(f"{b_wall} -|-----------------||-----------------|- {b_wall}")
    print(f"{b_wall} +| A B C D E F G H || A B C D E F G H |+ {b_wall}")
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{full_block()}\n")


def message_generator(player_target, comp_target):
    """
    generates messages depending on the outcome of the turn
    """
    msg_1a = "            WE HAVE BEEN STRUCK COMMANDER! SUB "
    msg_1b = f"{comp_target[1]}{comp_target[2]} HAS BEEN DOMINATED"
    msg_2a = "            WE HAVE OUTMANOEUVRED THE ENEMY'S STRIKE AT "
    msg_2b = f"{comp_target[1]}{comp_target[2]} COMMANDER"
    create_board()
    if player_target in "X":
        print("                    ----WE STRUCK THE ENEMY, COMMANDER.----\n")
    else:
        print("                   ---NO ENEMY AT COORDINATES, COMMANDER.---\n")

    if comp_target[0] in "X":
        print(f"{msg_1a}{msg_1b}")
    else:
        print(f"{msg_2a}{msg_2b}")


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
        print(f"          COMMANDER SUBS REMAINING : {player_shipcount}     ||     {comp_shipcount} : AI SUBS REMAINING")
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
