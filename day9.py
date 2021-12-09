f = open("datenday9", "r")
listItems = f.read().split("\n")

print(listItems)
xlength = len(listItems[0])

def splititem(item):
    return [letter for letter in item]

for i_list in range(len(listItems)):
    above = []
    under = []
    current = []
    if i_list == 0:
        current = splititem(listItems[i_list])
        under = splititem(listItems[i_list + 1])
        start = 100
        for i_number in range(len(current)):
            move = 0
            if i_number == 0:
                for i_inlist in [0, 1]:
                    if current[i_number + i_inlist] < start:
                        start = current[i_number + i_inlist]
                        move = 1
                    if under[i_number + i_inlist] < start:
                        start = under[i_number + i_inlist]
                        move = 1
            elif i_number == len(current) - 1:
                for i_inlist in [0, -1]:
                    if current[i_number + i_inlist] < start:
                        start = current[i_number + i_inlist]
                        move = 1
                    if under[i_number + i_inlist] < start:
                        start = under[i_number + i_inlist]
                        move = 1
            else:
                for i_inlist in [0, -1, 1]:
                    if current[i_number + i_inlist] < start:
                        start = current[i_number + i_inlist]
                        move = 1
                    if under[i_number + i_inlist] < start:
                        start = under[i_number + i_inlist]
                        move = 1

        print("1.")
        print(current)
        print(under)
    elif i_list == len(listItems) - 1:
        current = splititem(listItems[i_list])
        above = splititem(listItems[i_list - 1])
        print("2.")
        print(above)
        print(current)
    else:
        print("3.")
        current = splititem(listItems[i_list])
        above = splititem(listItems[i_list - 1])
        under = splititem(listItems[i_list + 1])
        print(above)
        print(current)
        print(under)





    #for i_number in listItems[i_list]:
    #    if i_list == 0 or i_list == len(listItems):
    #        if listItems[i_list].find(i_number) == 0 or listItems[i_list].find(i_number) == len(listItems[i_list])