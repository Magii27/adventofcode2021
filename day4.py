f = open("datenday4", "r")
listItems = f.read().split("\n")
numbers = list(map(int,listItems[0].split(",")))
listItems.remove(listItems[0])


def checkwin(board, boardcount, row1, index):
    key = str(boardcount) + "_"
    for row in range(1, 6):
        if board[key + str(row)][index] != "X":
            break
    else:
        return True, boardcount

    for column in range(0, 5):
        if board[key + str(row1)][column] != "X":
            break
    else:
        return True, boardcount

    return False, ""


boardcount = 1
board = {}
i = 0

while i < len(listItems):
    for counter in range(1, 6):
        templist = listItems[i + counter].split(" ")
        while True:
            if "" in templist:
                templist.remove("")
            else:
                break
        board[str(boardcount) + "_" + str(counter)] = list(map(int, templist))
    boardcount += 1
    i += 6

pruefung = False
bcount = boardcount
boardcount = 1

for number in numbers:
    winnum = number
    for x in range(1, bcount):
        for row in range(1, 6):
            if number in board[str(x) + "_" + str(row)]:
                index = board[str(x) + "_" + str(row)].index(number)
                board[str(x) + "_" + str(row)][index] = "X"
                #print(board)
                pruefung, board1 = checkwin(board, x, row, index)
                if pruefung is True:
                    print("sieger")
                    boardsieger ={}
                    for k in range(1, 6):
                        boardsieger[str(k)] = board[str(board1) + "_" + str(k)]

                    print(boardsieger)
                    break
            boardcount += 1
        if pruefung is True:
            break
    if pruefung is True:
        break

ergebnis = 0

for key in boardsieger.keys():
    for item in range(0, 5):
        if boardsieger[key][item] != "X":
            ergebnis += boardsieger[key][item]

print(ergebnis, winnum, ergebnis * winnum)


boardcount = 0
board = {}
i = 0

while i < len(listItems):
    boardcount += 1
    for counter in range(1, 6):
        templist = listItems[i + counter].split(" ")
        while True:
            if "" in templist:
                templist.remove("")
            else:
                break
        board[str(boardcount) + "_" + str(counter)] = list(map(int, templist))
    i += 6

pruefung = False
countwinning = 0
test1 = False
test = False
check = []

for o in range(1, boardcount + 1):
    check.append(o)
    print(o)

check1 = check.copy()

for number in numbers:
    winnum = number
    check = check1.copy()
    for x in check:
        for row in range(1, 6):
            if number in board[str(x) + "_" + str(row)]:
                index = board[str(x) + "_" + str(row)].index(number)
                board[str(x) + "_" + str(row)][index] = "X"
                pruefung, board1 = checkwin(board, x, row, index)

                if pruefung is True:
                    countwinning += 1

                    if countwinning == 100:
                        test = True
                        print("sieger")
                        boardsieger = {}

                        for k in range(1, 6):
                            boardsieger[str(k)] = board[str(board1) + "_" + str(k)]
                            print(boardsieger)
                    check1.remove(board1)

        if test is True:
            break

    if test is True:
        break

ergebnis = 0

for key in boardsieger.keys():
    for item in range(0, 5):
        if boardsieger[key][item] != "X":
            ergebnis += boardsieger[key][item]

print(ergebnis, winnum, ergebnis * winnum)