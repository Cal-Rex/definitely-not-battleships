def pick_coords():
    column_guess = str(input("pick a lettered column between A - H: ")).lower()
    while column_guess not in "abcdefgh" or column_guess.isdigit():
        print("you entered bad coords captain, try again!\n")
        column_guess = str(input("pick a lettered column between A - H: ")).lower()

    print(column_guess)
    column_guess_converted = ord(column_guess) - 96
    print(column_guess_converted)


    row_guess = input("pick a numbered row between 1 - 5: ")
    while row_guess not in "12345":
        print("you entered bad coords captain, try again!\n")
        row_guess = input("pick a numbered row between 1 - 5: ")

    row_guess = int(row_guess)
    print(row_guess)

p_row_1 = ["1|", "~", "~", "~", "~", "~", "~", "~", "~"]
p_row_2 = ["2|", "~", "~", "~", "~", "~", "~", "~", "~"]
p_row_3 = ["3|", "~", "~", "~", "~", "~", "~", "~", "~"]
p_row_4 = ["4|", "~", "~", "~", "~", "~", "~", "~", "~"]
p_row_5 = ["5|", "~", "~", "~", "~", "~", "~", "~", "~"]

c_row_1 = ["|1", "~", "~", "~", "~", "~", "~", "~", "~"]
c_row_2 = ["|2", "~", "~", "~", "~", "~", "~", "~", "~"]
c_row_3 = ["|3", "~", "~", "~", "~", "~", "~", "~", "~"]
c_row_4 = ["|4", "~", "~", "~", "~", "~", "~", "~", "~"]
c_row_5 = ["|5", "~", "~", "~", "~", "~", "~", "~", "~"]


def create_board():
    print("+| A B C D E F G H | A B C D E F G H |+")
    print("-|-----------------|-----------------|-")
    print(" ".join(p_row_1), "|", " ".join(c_row_1[1:]), c_row_1[0])
    print(" ".join(p_row_2), "|", " ".join(c_row_2[1:]), c_row_2[0])
    print(" ".join(p_row_3), "|", " ".join(c_row_3[1:]), c_row_3[0])
    print(" ".join(p_row_4), "|", " ".join(c_row_4[1:]), c_row_4[0])
    print(" ".join(p_row_5), "|", " ".join(c_row_5[1:]), c_row_5[0])
    print("-|-----------------|-----------------|-")
    print("+| A B C D E F G H | A B C D E F G H |+\n")


create_board()
pick_coords()