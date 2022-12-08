import os
import random
from termcolor import colored, cprint


def red_txt(string):
    """
    turns string text color to red with short name
    to improve code concatenation
    """
    statement = colored(string, "red")
    return statement


def grn_txt(string):
    """
    turns string text color to green short name
    to improve code concatenation
    """
    statement = colored(string, "green")
    return statement


def cya_txt(string):
    """
    turns string text color to cyan short name
    to improve code concatenation
    """
    statement = colored(string, "cyan")
    return statement


def clear_terminal():
    """
    Clears the terminal between actions
    to stop unnecessary scrolling and clutter
    """
    os.system('clear')


def full_block():
    """
    creates a full line of █
    """
    string = ""
    for _ in range(0, 80):
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
    line_7a = f"█/          /█ {red_txt('M   A   R   I   N   E')} ██"
    line_7b = f"██ {red_txt('I   N   A   T   I   O   N')}"
    line_7c = r" █\   \\   \█"
    line_8a = r"█__________/███ T A C T I C A L █ M A R I N E █"
    line_8b = r" E S P I O N A G E ████\___\\___█"

    print(full_block())
    print(f"{line_1a}{line_1b}")
    print(f"{line_2a}{line_2b}")
    print(f"{line_3a}{line_3b}")
    print(f"{line_4a}{line_4b}")
    print(f"{line_5a}{line_5b}")
    print(f"{line_6a}{line_6b}")
    print(f"{line_7a}{line_7b}{line_7c}")
    print(f"{line_8a}{line_8b}")
    print(full_block())


def player_lose():
    """
    executes loss message and input option
    to restart game or return to title
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
    l_space = r"       "
    msg_1a = r"         THE ENEMY DOMINATED ALL OF OUR"
    msg_1b = r" SUBS COMMANDER. WE HAVE LOST."
    error_msg1 = f"                 {red_txt('COMMANDS ARE UNCLEAR')}"
    error_msg2 = f" {red_txt('COMMANDER, PLEASE ANSWER')}\n"
    clear_terminal()
    cprint(full_block(), "red")
    print(f"{l_space}{exp_1}")
    print(f"{l_space}{exp_2}")
    print(f"{l_space}{exp_3}")
    print(f"{l_space}{exp_4}")
    print(f"{l_space}{exp_5}")
    print(f"{l_space}{exp_6}")
    print(f"{l_space}{exp_7}")
    print(f"{l_space}{exp_8}")
    print(f"{l_space}{exp_9}")
    print(f"{l_space}{exp_10}")
    print(f"{l_space}{exp_11}")
    print(f"{l_space}{exp_12}")
    print(f"{l_space}{exp_13a}{exp_13b}")
    cprint(full_block(), "red")
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
    executes win message and gives input option
    to restart the game or return to title
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
    msg_align_1 = "                     "
    msg_align_2 = "                                  "
    inpt_align = r"                           "

    clear_terminal()
    cprint(full_block(), "green")
    print(space + sub_1)
    print(space + sub_2)
    print(space + sub_3)
    print(space + sub_4)
    print(space + sub_5)
    print(space + sub_6)
    print(space + sub_7a + sub_7b)
    print(space + sub_8a + sub_8b)
    print(space + sub_9a + sub_9b)
    cprint(full_block(), "green")

    print(f"{msg_align_1}WE HAVE DOMINATED ALL ENEMY SUBS, COMMANDER")
    print(f"{msg_align_2}WE HAVE WON")

    query_new_game = str(input(f"{inpt_align}NEW GAME? Y/N: ")).lower()
    while query_new_game not in "yn":
        print(f"{red_txt('COMMANDS ARE UNCLEAR COMMANDER, PLEASE ANSWER')}\n")
        query_new_game = str(input("NEW GAME? Y/N: ")).lower()
    if query_new_game == "y":
        main()
    else:
        title_menu()


def hit_checker(row, col, col_str):
    """
    Checks to value of player targeted row and col,
    and sees if a coordinate has been targeted before.
    prints statement depending on outcome
    """
    err_msg_sp1 = "              "
    err_msg_sp2 = "                "
    err_msg_sp3 = "             "
    err_msg_1a = "WE HAVE ALREADY NEUTRALIZED THREATS AT"
    err_msg_1b = f" {col_str.upper()}{row}, COMMANDER"
    err_msg_2a = f"COORDINATES {col_str.upper()}{row} "
    err_msg_2b = "HAVE ALREADY BEEN STRUCK, COMMANDER"
    err_msg_3a = "WE SHOULD CONSERVE OUR ORDINANCE"
    err_msg_3b = ", THINK OF THE BUDGET\n"

    if C_BOARD[row][col] == "X":
        print(f"{err_msg_sp1}{err_msg_1a}{err_msg_1b}")
        did_it_hit = True
    elif C_BOARD[row][col] == ".":
        create_board()
        print(f"{err_msg_sp2}{err_msg_2a}{err_msg_2b}")
        print(f"{err_msg_sp3}{err_msg_3a}{err_msg_3b}")
        did_it_hit = True
    else:
        did_it_hit = False

    return did_it_hit


def pick_coords(game_in_play):
    """
    Allows player to input coordinates by using input
    fields to pick a column, then row.
    identifies when values would cause an error
    and prints messages as appropriate
    """
    wa_print_1 = red_txt("                    COMMANDER,")
    wa_print_2 = red_txt(" THESE ARE INVALID COORDINATES")

    cga_print_1a = red_txt("                      WE ")
    cga_print_1b = red_txt("MUST TARGET A COLUMN ON THE RADAR\n")
    cga_print_2a = red_txt("                WE MUST POSITION")
    cga_print_2b = red_txt(" OUR SUBS WITHIN VISIBLE COLUMNS\n")
    cga_print_3a = "                       "
    cga_print_3b = "DESIGNATE RADAR COLUMN, COMMANDER"

    cg_str = grn_txt(" pick a lettered column between A - H: ")

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
                    print(f"{wa_print_1}{wa_print_2}")
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
        rga_print_1a = red_txt("                WE MUST STRIKE AN UN-TARGETED")
        rga_print_1b = red_txt(f" ROW IN COLUMN {column_guess.upper()}\n")
        rga_print_2a = red_txt("                 WE MUST POSITION OUR SUB IN ")
        rga_print_2b = red_txt(f"A ROW ON COLUMN {column_guess.upper()}\n")
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
                    print(f"{wa_print_1}{wa_print_2}")
                    if game_active is True:
                        print(f"{rga_print_1a}{rga_print_1b}")
                    else:
                        print(f"{rga_print_2a}{rga_print_2b}")
                if game_active is True:
                    print(f"{rga_print_3a}{rga_print_3b}")
                    print(f"{rga_print_3c}{rga_print_3d}")
                else:
                    print(f"{rga_print_4a}{rga_print_4b}{rga_print_4c}")
                row_guess = str(input(grn_txt(" pick a row between 1 - 5: ")))
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
    prints messages if player enters invalid coords or duplicates
    """
    loop_1_txt = "                    ---POSITION SUB NUMBER  "
    loop_2_txta = red_txt("            COMMANDER, WE HAVE ALREADY")
    loop_2_txtb = red_txt(" DEPLOYED AT THESE COORDINATES")
    loop_2_txtc = red_txt("                    WE MUST EMPLOY")
    loop_2_txtd = red_txt(" TACTICAL MARINE ESPIONAGE")
    loop_2_txte = red_txt("                    PLEASE RECONSIDER ")
    game_in_play = False
    rows = []
    cols = []
    for i in range(5):
        print(f"{loop_1_txt}{i + 1}, COMMANDER---")
        row, col = pick_coords(game_in_play)
        rows.append(row)
        cols.append(col)

        while P_BOARD[row][col] == "@":
            create_board()
            print(f"{loop_2_txta}{loop_2_txtb}")
            print(f"{loop_2_txtc}{loop_2_txtd}")
            print(f"{loop_2_txte}{red_txt('COORDINATES FOR SUB')} {i + 1}:\n")
            row, col = pick_coords(game_in_play)

        P_BOARD[row][col] = "@"
        create_board()
    return True, rows, cols


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
    function for computer's turn
    allows computer to pick 2 random numbers within appropriate ranges
    on turns 3, 7, 11, 15, 18, comp will auto guess player's sub
    """
    print(p_rows)
    print(p_columns)
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
    runs sequence that allows players to
    choose coordinates to strike
    takes returned values of called functions to determine a hit or miss
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
    msg_1a = red_txt("            WE HAVE BEEN STRUCK COMMANDER! SUB ")
    msg_1b = red_txt(f"{comp_target[1]}{comp_target[2]} HAS BEEN DOMINATED")
    msg_2a = grn_txt("           WE HAVE OUTMANOEUVRED THE ENEMY'S STRIKE AT ")
    msg_2b = grn_txt(f"{comp_target[1]}{comp_target[2]} COMMANDER")
    create_board()
    if player_target in "X":
        c_align = "                    "
        cprint(f"{c_align}----WE STRUCK THE ENEMY, COMMANDER.----\n", "green")
    else:
        print("                   ---NO ENEMY AT COORDINATES, COMMANDER.---\n")

    if comp_target[0] in "X":
        print(f"{msg_1a}{msg_1b}")
    else:
        print(f"{msg_2a}{msg_2b}")


def main():
    """
    main function that runs the whole game
    establishes global variables
    houses the game board in 2 dicts
    keeps track of ship counts for player and comp
    by seperate variables
    keeps track of turns taken
    calls core gamplayloop functions
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

    game_start, p_rows, p_columns = position_subs()

    while player_shipcount > 0:
        if comp_shipcount == 0:
            break
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
        msg_gen_1 = f"      COMMANDER SUBS REMAINING : {player_shipcount}  "
        msg_gen_2 = f"   ||     {comp_shipcount} : AI SUBS REMAINING"

        print(f"{msg_gen_1}{msg_gen_2}")
        turns += 1

    if comp_shipcount == 0:
        player_win()
    else:
        player_lose()


def game_info_exp():
    """
    explains game rules and mechanics to user/player
    prints explanation and game diagram to terminal
    """
    b_perim = "                                          "
    b_wall = "█                 █"
    concat_line_1a = "█   WELCOME TO    █ +| A B C D E F G H ||"
    concat_line_1b = " A B C D E F G H |+ █        THIS IS  █"
    concat_line_2a = f"█   {red_txt('SUBMARINE')}     █ -|-----------------||"
    concat_line_2b = "-----------------|- █  AN EXAMPLE OF  █"
    concat_line_3a = f"█   {red_txt('DOMINATION')}    █ 1| ~ @ ~ ~ @ ~ ~ ~ ||"
    concat_line_3b = " ~ ~ X ~ ~ ~ ~ ~ |1 █  THE SIMULATED  █"
    concat_line_4a = "█   SIMULATION    █ 2| ~ ~ ~ ~ ~ ~ @ ~ ||"
    concat_line_4b = " ~ ~ ~ ~ ~ ~ ~ ~ |2 █          ARENA  █"
    concat_line_5a = "█   COMMANDER     █ 3| ~ ~ ~ ~ ~ ~ ~ ~ ||"
    concat_line_5b = f" ~ ~ ~ ~ . ~ ~ ~ |3 {b_wall}"
    concat_line_6a = f"{b_wall} 4| ~ ~ ~ X ~ ~ ~ ~ ||"
    concat_line_6b = " ~ ~ ~ ~ ~ ~ ~ ~ |4 █    ENEMY SUBS   █"
    concat_line_7a = f"█ [{grn_txt('LEFT')}] IS YOUR  █ 5| ~ . ~ ~ ~ ~ @ ~ ||"
    concat_line_7b = f" ~ ~ ~ ~ ~ ~ ~ ~ |5 █ARE HIDDEN[{red_txt('RIGHT')}]█"
    concat_line_8a = "█      ZONE       █ -|-----------------||"
    concat_line_8b = "-----------------|- █ . = MISSED SHOT █"
    concat_line_9a = "█ @ = YOUR SHIPS  █ +| A B C D E F G H ||"
    concat_line_9b = " A B C D E F G H |+ █  X = SUNK SUB   █"

    explain_line_1a = "         AT THE START OF THE GAME, "
    explain_line_1b = f"YOU WILL BE ASKED TO POSITION {red_txt('5')} SUBS"

    explain_line_6a = "      YOU WILL THEN USE THIS SAME "
    explain_line_6b = "PROCESS TO PREDICT ENEMY SUB PLACEMENT"
    explain_line_7a = f"    THE {red_txt('HIGHLY ADVANCED AI')} WILL "
    explain_line_7b = "IN-TURN ATTEMPT TO PREDICT YOUR HIDDEN SUBS"
    explain_line_8a = "          SIMULATION STEPS REPEAT "
    explain_line_8b = f"UNTIL ALL {red_txt('5')} "
    explain_line_8c = f"ENEMY SUBS ARE {red_txt('DOMINATED')}"
    explain_line_9a = "                      OR"
    explain_line_9b = f" ENEMY {red_txt('DOMINATES')} ALL"
    explain_line_9c = f" {red_txt('5')} OF YOUR SUBS"

    conc_exp_1c = f"\n                      +|       {grn_txt('X')}:  "
    conc_exp_1d = "Return to Title       |+"

    print(full_block())
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{concat_line_1a}{concat_line_1b}")
    print(f"{concat_line_2a}{concat_line_2b}")
    print(f"{concat_line_3a}{concat_line_3b}")
    print(f"{concat_line_4a}{concat_line_4b}")
    print(f"{concat_line_5a}{concat_line_5b}")
    print(f"{concat_line_6a}{concat_line_6b}")
    print(f"{concat_line_7a}{concat_line_7b}")
    print(f"{concat_line_8a}{concat_line_8b}")
    print(f"{concat_line_9a}{concat_line_9b}")
    print(f"{b_wall}{b_perim}{b_wall}")
    print(f"{full_block()}")
    print(f"{explain_line_1a}{explain_line_1b}")
    print("              LIKE THIS:")
    print(f"               {grn_txt('pick a lettered column between A - H:')}")
    print("              THEN LIKE THIS:")
    print(f"               {grn_txt('pick a numbered row between 1 - 5:')}")
    print(f"{full_block()}")
    print(f"{explain_line_6a}{explain_line_6b}")
    print(f"{explain_line_7a}{explain_line_7b}")
    print(f"{explain_line_8a}{explain_line_8b}{explain_line_8c}")
    print(f"{explain_line_9a}{explain_line_9b}{explain_line_9c}")
    print(f"{conc_exp_1c}{conc_exp_1d}")


def menu_option(title):
    """
    displays menu options and allows user to select a new game or instructions
    will print message if incorrect input entered
    """
    conc_exp_1a = f"                      +| {grn_txt('N')}: New Game |  | "
    conc_exp_1b = f"{grn_txt('I')}: How to Play |+"
    conc_inc_1a = "               INVALID CHOICE, "
    conc_inc_1b = "PLEASE PICK FROM SPECIFIED OPTIONS\n"
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
                print(f"{conc_exp_1a}{conc_exp_1b}")
                print(f"{conc_inc_1a}{conc_inc_1b}")
            else:
                print(f"{conc_exp_1a}{conc_exp_1b}")

            opt = str(input(f"{grn_txt('pick an option above:')} ")).lower()
            if opt not in "nix" or opt.isdigit():
                raise ValueError()
            elif len(opt) < 1:
                raise ValueError()
            elif len(opt) > 1:
                raise ValueError()
        except ValueError:
            wrong_option_value = True
        else:
            title_option_select = True
    wrong_option_value = False

    if opt == "n":
        main()
    elif opt == "i":
        game_info()
    else:
        title_menu()


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
