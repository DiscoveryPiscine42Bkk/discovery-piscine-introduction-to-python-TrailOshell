from checkmate import checkmate
SC = "Success\n"
FL = "Fail\n"
ER = "Error\n"

import io
from contextlib import redirect_stdout

NCL = "\033[0;39m"
RED = "\033[0;91m"
GRN = "\033[0;92m"
YLW = "\033[0;93m"
BLU = "\033[0;94m"
PUR = "\033[0;95m"
CYN = "\033[0;96m"

def testmate(board, expect, case):

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        checkmate(board)
    output = buffer.getvalue()

    if expect == ER and (output == "" or output.strip() == ""):
            print(f"{GRN}OK {NCL}", end="")
    elif output.lower() == expect.lower() :
        print(f"{GRN}OK {NCL}", end="")
    else:
        print(f"\n")
        print(f"{YLW}Case: {PUR}{case} {NCL}")
        try:
            print(f"{CYN}", end="")
            for row in board.split():
                print(row)
            print(f"{NCL}", end="")
        except:
            print("", end="")
        print(f"\n{CYN}output {NCL}\"{output[:-1]}\" \n{YLW}expect {NCL}\"{expect[:-1]}\"")
        if expect == ER:
            print(f"{YLW}ER {NCL}")
        else:
            print(f"{RED}KO {NCL}")
    
def cases_error():
    print(f"{PUR}Error Checks{NCL}")
    
    board = """\
    R.....
    .K...Q
    ......
    ......\
    """
    testmate(board, ER, "uneven 4x6 board")
    
    print(f"\n")

def cases_king_count():
    print(f"{PUR}Only one King Checks{NCL}")
    
    board = """\
    ...
    ...
    .P.\
    """
    testmate(board, ER, "no king")
    
    board = """\
    ...
    K.K
    .P.\
    """
    testmate(board, ER, "two king")
    
    board = """\
    .K.
    K.K
    .P.\
    """
    testmate(board, ER, "three king")
    
    print(f"\n")

def cases_success():
    print(f"{PUR}Success Checks{NCL}")
    
    board = """\
    ....K
    .....
    ..Q..
    .....
    .....\
    """
    testmate(board, SC, "Queen check King")

    board = """\
    R...
    .K.Q
    ....
    ....\
    """
    testmate(board, SC, "A board")
    
    board = """\
    Q...
    ....
    ....
    ...K\
    """
    testmate(board, SC, "Check from furthest of board diagonally (Success)")

    board = """\
    ....
    ....
    ....
    Q..K\
    """
    testmate(board, SC, "Check from furthest of board horizontally (Success)")
    
    print(f"\n")

def cases_fail():
    print(f"{PUR}Fail Checks{NCL}")
    board = """\
    ..PK
    ....
    ....
    ....\
    """
    testmate(board, FL, "Pawn next to King")

    board = """\
    ..
    .K\
    """
    testmate(board, FL, "Just King")

    board = """\
    ....
    .K..
    ....
    ...P\
    """
    testmate(board, FL, "Pattern out of bound")

    board = """\
    ....
    .K..
    ....
    ..R.\
    """
    testmate(board, FL, "No path to King")

    print(f"\n")

def cases_obstruct():
    print(f"{PUR}blocked path Checks{NCL}")
    
    board = """\
    ....
    .K..
    .P..
    .R..\
    """
    testmate(board, FL, "Other piece obstruct King")
    
    board = """\
    ....
    .K.R
    PPP.
    .R..\
    """
    testmate(board, SC, "a piece obstruct but still check")
    
    print(f"\n")

def cases_odd_chars():
    print(f"{PUR}Odd character Checks{NCL}")
    board = """\
    ....
    .Kk.
    ..P.\
    """
    testmate(board, ER, "lowercase k")

    print(f"\n")

def cases_not_string():
    print(f"{PUR}Odd character Checks{NCL}")
    board = 1234567890
    testmate(board, ER, "numbers")

    print(f"\n")


def main():
    cases_error()
    cases_king_count()
    cases_success()
    cases_fail()
    cases_obstruct()
    cases_odd_chars()
    cases_not_string()

if __name__ == "__main__":
    main()