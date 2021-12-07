import statistics as s
f = open("datenday7", "r")
listItems = list(map(int, f.read().split(",")))

print("----Advent of Code Day 7----")

#---- PART ONE----#
common = int(s.median(listItems))
#print("Median for part one: ", common)

fuel = 0
for item in listItems:
    if item > common:
        for i in range(common, item):
            fuel += 1
    else:
        for i in range(item, common):
            fuel += 1

print("Answer for part one: ", fuel)


#---- PART TWO ----#
common = int(sum(listItems)/len(listItems))
#print("Average for part two: ", common)

fuel = 0
for item in listItems:
    zaehler = 0
    if item > common:
        for i in range(common, item):
            fuel += 1 + zaehler
            zaehler += 1
    else:
        for i in range(item, common):
            fuel += 1 + zaehler
            zaehler += 1

print("Answer for part two: ", fuel)



