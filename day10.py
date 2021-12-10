import statistics
f = open("datenday10", "r")
listItems = f.read().split("\n")

print(listItems)

liste = {"(":")", "[":"]", "{":"}", "<":">"}
points = {"0":0,")":3, "]":57, "}":1197, ">":25137}
pointspart2 = {")":1, "]":2, "}":3, ">":4}
opens = ["(", "[", "{", "<"]
part2 = []

def get_lastindex(liste, item_to_find):
    index = 0
    for i in range(len(liste)):
        item = liste[i]
        if item == item_to_find:
            index = i

    return index


qeue = []
ergebnispart1 = 0
for item in listItems:
    search = "0"
    for bracket in item:
        if bracket in opens:
            print(qeue)
            qeue.append(bracket)
        else:
            print("item: ", item)
            print("Expected: ", liste[str(qeue[len(qeue) - 1])])
            print("Found: ", bracket)
            if liste[str(qeue[len(qeue) - 1])] != bracket:
                print("Bracket ist wrong: ", bracket)
                search = bracket
                break
            elif qeue.count(bracket) > 1:
                print("1Qeue before pop: ", qeue)
                qeue.pop(len(qeue) - 1)
                print("1Qeue after pop: ", qeue)
            else:
                print("Qeue before pop: ", qeue)
                qeue.pop(len(qeue) - 1)
                print("Qeue after pop: ", qeue)

    ergebnispart1 += points[search]
    part2ergebnis = 0

    if search == "0":
        for i in range(len(qeue)):
            part2ergebnis *= 5
            part2ergebnis += pointspart2[liste[qeue[(len(qeue) - 1) - i]]]
            #print(qeue[(len(qeue) - 1) - i])
        part2.append(part2ergebnis)
    qeue.clear()

part2.sort()
print(part2)
print("median part2: ", statistics.median(part2))
print(ergebnispart1)