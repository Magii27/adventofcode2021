f = open("datenday3", "r")
listItems = f.read().splitlines()

print("----Advent of Code Day 3----")

#---- PART ONE ----#
zero = []
one = []
gamma = ""
epsilon = ""

for i in range(0, 12):
    zero.append(0)
    one.append(0)

for item in listItems:
    zaehler = 0
    for digit in item:
        if digit == "0":
            zero[zaehler] += 1
        else:
            one[zaehler] += 1
        zaehler += 1

for i in range(len(zero)):
    if zero[i] > one[i]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_rate = int(gamma, 2)
epsilon_rate = int(epsilon, 2)
power_consumption = gamma_rate * epsilon_rate

print("Answer for part one: ", power_consumption)

#---- PART TWO ----#
def getbinary(itemlist, dominantnum):
    items = itemlist.copy()
    position = 0
    while True:
        count_zero = 0
        count_one = 0
        remove = []
        for item in items:
            if item[position:position + 1] == "0":
                count_zero += 1
            else:
                count_one += 1

        if dominantnum == "1":
            if count_zero > count_one:
                delete = "1"
            else:
                delete = "0"
        else:
            if count_one < count_zero:
                delete = "0"
            else:
                delete = "1"

        for item in items:
            if item[position:position + 1] == delete:
                remove.append(item)

        for item in remove:
            items.remove(item)

        if len(items) == 1:
            break
        position += 1

    return items[0]


oxygen_binary = getbinary(listItems, "1")
co2_binary = getbinary(listItems, "0")

oxygen = int(oxygen_binary, 2)
co2 = int(co2_binary, 2)

lifesupport = oxygen * co2

print("Answer for part two: ", lifesupport)
