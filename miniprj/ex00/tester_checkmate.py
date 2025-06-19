import io
from contextlib import redirect_stdout
from checkmate import checkmate

SC = "Success\n"
FL = "Fail\n"
ER = "Error\n"

NCL = "\033[0;39m"
RED = "\033[0;91m"
GRN = "\033[0;92m"
YLW = "\033[0;93m"
BLU = "\033[0;94m"
PUR = "\033[0;95m"
CYN = "\033[0;96m"

def testmate(board, expect, case):
    # print(f"{YLW}Case: {PUR}{case}{NCL}")

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        checkmate(board)
    
    output = buffer.getvalue()
    if output.lower() == expect.lower() :
        print(f"{GRN}OK {NCL}", end="")
    else:
        print(f"\n")
        print(f"{CYN}", end="")
        for row in board.split():
            print(row)
        print(f"{NCL}", end="")
        print(f"{RED}KO {NCL}", end="")
        print(f"-> {YLW}Case: {PUR}{case} {NCL}", end="")
        print(f"output \"{output[:-1]}\" expect \"{expect[:-1]}\"\n")
    
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

    board = """\
    ....
    .K..
    .P..
    .R..\
    """
    testmate(board, FL, "Other piece obstruct King")

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

def main():
    cases_error()
    cases_king_count()
    cases_success()
    cases_fail()
    cases_odd_chars()

if __name__ == "__main__":
    main()