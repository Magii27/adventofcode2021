f = open("datenday8", "r")
listItems = f.read().split("\n")

output_value = {}
signal_patterns = {}

for i in range(len(listItems)):
    pattern = listItems[i][:listItems[i].find("|") - 1].split(" ")
    values = listItems[i][listItems[i].find("|") + 2:].split(" ")

    signal_patterns[i] = pattern
    output_value[i] = values

#0 d e a g b c
#1 a f
#2 d a f g c
#3 d a f b c
#4 e a f b
#5 d e f b g
#6 d e f g b c
#7 d a b
#8 d e a f g b c
#9 d e a f b c
"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa       0000
b    .  b    .  .    c  b    c  b    c     1    2
b    .  b    .  .    c  b    c  b    c     1    2
 dddd    dddd    ....    dddd    dddd       3333
.    f  e    f  .    f  e    f  .    f     4    5
.    f  e    f  .    f  e    f  .    f     4    5
 gggg    gggg    ....    gggg    gggg       6666
 """
segment_num_part2 = {0:[0, 1, 2, 4, 5, 6], 1:[2, 5], 2:[0, 2, 3, 4, 6], 3:[0, 2, 3, 5, 6],
                   4:[1, 2, 3, 5], 5:[0, 1, 3, 5, 6], 6:[0, 1, 3, 4, 5, 6], 7:[0, 2, 5],
                   8:[0, 1, 2, 3, 4, 5, 6], 9:[0, 1, 2, 3, 5, 6]}

segment_clear = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
#segment_part2 = {0:["a", "b", "c", "e", "d", "g"], 1:["a", "f"], 2:["a", "c", "d", "f", "g"],
                 #3:["a", "c", "d", "f", "b"], 4:["b", "e", "a", "f"], 5:["e", "b", "d", "f", "g"],
                 #6:["c", "b", "d", "e", "f", "g"], 7:["d", "a", "b"], 8:["a", "b", "c", "d", "e", "f", "g"],
                 #9:["a", "b", "c", "d", "f", "e"]}


letters = ["a", "b", "c", "d", "e", "f", "g"]
for i  in range(len(signal_patterns)):
    signal_patterns[i] = list(sorted(signal_patterns[i], key=len))

print(signal_patterns)
print(output_value)

def get_pattern(signal_pattern, segment_list, segment_list3):
    segment_list2 = segment_list3.copy()
    to_add_index = []
    to_add_letter = []
    for i in range(0, 10):
        if i == 0:
            to_add_index.append(2)
            to_add_index.append(5)
            for letter in signal_pattern[i]:
                to_add_letter.append(letter)
        elif i == 1:
            to_add_index.append(0)
            for letter in signal_pattern[i]:
                if letter in to_add_letter:
                    continue
                to_add_letter.append(letter)
        elif i == 2:
            to_add_index.append(1)
            to_add_index.append(3)
            for letter in signal_pattern[i]:
                if letter in to_add_letter:
                    continue
                to_add_letter.append(letter)
        elif i == 9:
            to_add_index.append(6)
            to_add_index.append(4)
            for letter in signal_pattern[i]:
                if letter in to_add_letter:
                    continue
                to_add_letter.append(letter)

    for key in segment_list.keys():
        for item in segment_list[key]:
            segment_list2[key].append(to_add_letter[to_add_index.index(item)])

    return segment_list2


ergebnis = 0
for i in range(len(output_value)):
    #hochzaehlen = ""
    vergleich = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    segment_list1 = segment_clear.copy()
    segment_list = get_pattern(signal_patterns[i], segment_num_part2, segment_list1)
    print(segment_list)

    for item_key in output_value.keys():
        hochzaehlen = ""
        for list_value in output_value[item_key]:
            #hochzaehlen = ""
            breakout = False
            print("länge: ", len(list_value))
            if 2 == len(list_value):
                hochzaehlen += "1"
            elif len(list_value) == 4:
                hochzaehlen += "4"
            elif len(list_value) == 3:
                hochzaehlen += "7"
            elif len(list_value) == 7:
                hochzaehlen += "8"
                #print(hochzaehlen)
            else:
                print("else")
                for key_segment in range(0, 10):
                    all_time_count = 0
                    length = (segment_list[key_segment])
                    count2 = 0
                    for letter_value in list_value:
                        count = 0
                        for item_segment_letter in segment_list[key_segment]:
                            if letter_value == item_segment_letter:
                                print("Buchstabe ist drinne: ", item_segment_letter)
                                count += 1
                                segment_w = key_segment
                                count2 += 1
                                break
                        else:
                            print("nicht gefunden")
                            count = 0
                            count2 += 1
                            break

                        all_time_count += count
                        #print("count: ", all_time_count, "count2: ", count2, len(segment_list[segment_w]))
                        if all_time_count == len(list_value) and count2 == len(segment_list[segment_w]):
                            #print("vor hochzaehlen: ", hochzaehlen, segment_w)
                            hochzaehlen += str(segment_w)
                            print("hochzaehlen: ", hochzaehlen)
                            breakout = True
                            break
                    if breakout is True:
                        print("break")
                        break

                       #print("all time count: ", all_time_count, "len: ", len(list_value))
                       #if count == len(list_value):
                       #    print("segfment beim hochz: ", str(segment_w))
                       #    hochzaehlen += str(segment_w)
                       #if breakout is True:
                       #    break


            #print(hochzaehlen)
    ergebnis += int(hochzaehlen)


    for key in segment_list.keys():
        segment_list[key].clear()

print(ergebnis)




#print(signal_patterns[1])

#ergebnis = 0
#for i in output_value.keys():
#    for item in output_value[str(i)]:
#        length = len(item)
#        print(length, item)
#        if length in segment_part1:
#            ergebnis += 1
#
#print(ergebnis)

output_value = {}
signal_patterns = {}

for i in range(len(listItems)):
    pattern = listItems[i][:listItems[i].find("|") - 1].split(" ")
    values = listItems[i][listItems[i].find("|") + 2:].split(" ")

    signal_patterns[i] = pattern
    output_value[i] = values

segment_part1 = [0, 2, 0, 0, 4, 0, 0, 3, 7, 0]
"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 """
ergebnis = 0
for i in output_value.keys():
    for item in output_value[i]:
        length = len(item)
        if length in segment_part1:
            ergebnis += 1

print(ergebnis)