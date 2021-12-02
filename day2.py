f = open("datenday2", "r")
listItems = f.read().splitlines()

print("----Advent of Code Day 2----")

#---- PART ONE ----#
hposition = 0
dposition = 0

for i in listItems:
    operation = i[:i.find(" ")]
    num = int(i[i.find(" ") + 1:])

    if operation == "forward":
        hposition += num
    elif operation == "up":
        dposition -= num
    else:
        dposition += num

answer = hposition * dposition
print("Answer for part one: ", answer)

#---- PART TWO ----#
aim = 0
hposition = 0
dposition = 0

for i in listItems:
    operation = i[:i.find(" ")]
    num = int(i[i.find(" ") + 1:])

    if operation == "forward":
        hposition += num
        dposition += aim * num
    elif operation == "up":
        aim -= num
    else:
        aim += num

answer = hposition * dposition
print("Answer for part two: ", answer)
