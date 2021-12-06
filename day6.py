f = open("datenday6", "r")
listItems = f.read().split(",")

print("----Advent of Code Day 2----")
print("Initial state: ", ", ".join(listItems))
listItems = list(map(int, listItems))


#---- PART ONE ----#
listItemspart2 = listItems.copy()
initial = listItemspart2.copy()
length = len(initial)

for i in range(1, 81):
    zaehler = 0
    #print("Str Day " + str(i) + ":", listItems)

    for j in range(len(listItemspart2)):
        if listItemspart2[j] == 0:
            listItemspart2[j] = 6
            listItemspart2.append(8)
            zaehler += 1
        else:
            listItemspart2[j] -= 1

    #print("End Day " + str(i) + ":", listItems)

print("Answer for part one: ", len(listItemspart2))


#---- PART TWO ----#
listItemspart1 = listItems.copy()
initial = listItemspart1.copy()
length = len(initial)

count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(initial)):
    count[numbers.index(listItemspart1[i])] += 1


for i in range(1, 257):
    new_six = count[0]

    for j in range(0, 9):
        if j == 6:
            count[j] = count[j + 1] + new_six
        elif j == 8:
            count[j] = new_six
        else:
            count[j] = count[j + 1]

print("Answer for part two: ", sum(count))
