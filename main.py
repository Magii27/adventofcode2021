f = open("datenday9", "r")
listItems = f.read().split("\n")

print(listItems)

listItems = [list(map(int, [liste for liste in listItems[i]]))for i in range(len(listItems))]
print(listItems)


def get_numbers(liste):
    lowestx1 = []
    lowesty1 = []
    checkx = []
    checky = []
    lowestx = ""
    lowesty = ""
    xlength = len(liste[0])
    ylength = len(liste)

    for range in (0, 2):
        for xi in range(xlength):
            zahl_temp = 10
            for yi in range(ylength):
                if liste[yi][xi] < zahl_temp:
                    zahl_temp = liste[yi][xi]
                    xcoordinate = xi
                    ycoordinate = yi
            lowestx1.append(xcoordinate)
            lowesty1.append(ycoordinate)
            checkx.append(xcoordinate)
            checky.append(ycoordinate)

            for yi in range(ylength):
                if liste[yi][xi] == zahl_temp and (xi not in checkx or yi not in checky):
                    lowestx1.append(xi)
                    lowesty1.append(yi)

            #lowestyx.append([liste for liste in add_toX.copy()])
            #lowestyy.append(add_toY.copy())
            checkx.clear()
            checky.clear()

        print("x: ")
        print(lowestx1)
        print(lowesty1)
        lowestx += lowestx1.copy()
        lowesty += lowesty1.copy()
        lowestx1.clear()
        lowesty1.clear()

    return lowestx, lowesty


x, y = get_numbers(listItems)
print(x)
print(y)

#for yi in range(ylength):
#    zahly_temp = 10
#    for xi in range(xlength):
#        if listItems[yi][xi] < zahly_temp:
#            zahly_temp = listItems[yi][xi]
#            xcoordinate = xi
#            ycoordinate = yi
#    lowestxx.append(xcoordinate)
#    lowestxy.append(ycoordinate)
#    checkx.append(xcoordinate)
#    checky.append(ycoordinate)
#
#    for xi in range(xlength):
#        if listItems[yi][xi] == zahly_temp and (xi not in checkx or not yi in checky):
#            lowestxx.append(xi)
#            lowestxy.append(yi)
#
#    #lowestxx.append(add_toX.copy())
#    #lowestxy.append(add_toY.copy())
#    checkx.clear()
#    checky.clear()
#
#print("y: ")
#print(lowestxx)
#print(lowestxy)
#lowestx = lowestyx + lowestxx
#lowesty = lowestyy + lowestxy
#print(lowestx)
#print(lowesty)
#skip = 0
#for i in range(len(lowestx)):
#    for i2 in range(len(lowesty)):
#        for item in lowestx[i]:
#            if lowestx[i][item] - lowestx[i + 1][item] in [0, 1, -1]:
#                print("passt")
#            else:
#                print("passt nicht")

