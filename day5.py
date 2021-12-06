f = open("datenday5", "r")
listItems = f.read().split("\n")

print("----Advent of Code Day 2----")

x1 = []
x2 = []
y1 = []
y2 = []

for item in listItems:
    one = item[:item.find(" ")]
    two = item[item.find(">") + 2:]
    x1.append(int(one[:one.find(",")]))
    x2.append(int(two[:two.find(",")]))
    y1.append(int(one[one.find(",") + 1:]))
    y2.append(int(two[two.find(",") + 1:]))


def getoverlap(x1, x2, y1, y2, listItems, diagonal):
    grid = []
    for i in range(0, 1000000):
        grid.append(0)

    for i in range(len(listItems)):
        if x1[i] != x2[i] and y1[i] != y2[i] and diagonal is False:
            continue
        else:
            if x2[i] - x1[i] < 0:
                x = -1
                xrange = x1[i] - x2[i]
            elif x2[i] - x1[i] > 0:
                x = 1
                xrange = x2[i] - x1[i]
            else:
                x = 0
                xrange = 0
            anfangx = x1[i]
            if y2[i] - y1[i] < 0:
                y = -1
                yrange = y1[i] - y2[i]
            elif y2[i] - y1[i] > 0:
                y = 1
                yrange = y2[i] - y1[i]
            else:
                y = 0
                yrange = 0
            anfangy = y1[i]
            if xrange != 0:
                for j in range(xrange + 1):
                    grid[1000*anfangy+anfangx] += 1
                    anfangx += x
                    anfangy += y
            else:
                for j in range(yrange + 1):
                    grid[1000*anfangy+anfangx] += 1
                    anfangx += x
                    anfangy += y

    ergebnis = 0
    for i in range(len(grid)):
        if grid[i] >= 2:
            ergebnis += 1

    return ergebnis


print("Answer for part one: ", getoverlap(x1, x2, y1, y2, listItems, False))

print("Answer for part one: ", getoverlap(x1, x2, y1, y2, listItems, True))