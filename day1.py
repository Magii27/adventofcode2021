f = open("datenday1", "r")
listItems = f.read().splitlines()
listItems = list(map(int, listItems))

print(listItems)

#---- PART TWO ----#
increased = 0
time = 1


def check(value1, value2):
    if value1 > value2:
        return 1

    return 0


for i in range(len(listItems)):
    try:
        if time == 1:
            first = listItems[i] + listItems[i+1] + listItems[i+2]
            if i != 0:
                increased += check(first, third)

        elif time == 2:
            second = listItems[i] + listItems[i + 1] + listItems[i + 2]
            increased += check(second, first)

        elif time ==3:
            third = listItems[i] + listItems[i + 1] + listItems[i + 2]
            increased += check(third, second)
            time = 0

        time += 1

    except IndexError:
        break

print(increased)

#----- PART ONE -----#
#increased = 0
#
#for i in range(1, len(listItems)):
#    if listItems[i] > listItems[i-1]:
#        increased += 1
#
#print(increased)