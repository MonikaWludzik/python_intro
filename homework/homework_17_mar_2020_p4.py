# Zadanie 2
# all columns equal
# width 30 / sliced and substitue with ...
# embedded list
#not finished needs some polishing

mainlist = ['masterpiece', 'centipede', 'skull', 'rest']
smainlist = (sorted(mainlist, key=len,reverse = True)) #sorting the list by len
item1 = smainlist[0]

def longest_value_in(row):
    lengths = [len(cell) for cell in row]  # transforming values in a list; comprehension!!! in other langs, called "mapping"
    return max(lengths)


def drawing_one_row(mainlist, cell_width, draw_top=True):
    longest = cell_width + 2

    toprow = [longest*"-" for i in mainlist] #looping the new list
    middlerow = [f" {i}".ljust(longest) for i in mainlist]

    if draw_top:
        print('+' + "+".join(toprow)    + '+') #join statement to print string for each item on the list
    print('|' + '|'.join(middlerow) + '|')
    print('+' + "+".join(toprow)    + '+')


def drawing_frames(header, rows):
    longest = longest_value_in(header)
    for row in rows:
        longest_in_row = longest_value_in(row)
        if longest_in_row > longest:
            longest = longest_in_row

    drawing_one_row(header, longest)
    for row in rows:
        drawing_one_row(row, longest, False)


# toprow = []
# for i in mainlist:
# toprow.append("+"+ len(item1)*"-" + "+") appending items to the list


# for i in range(smainlist):
#     i=+1
#     print(mainlist[i])
# #     print(i)

# for i in mainlist:
#     print(f"{i}"+"|")
# signs = print("+"+ (len(int(i+1))*"-" + "+"))

# for i in mainlist:
#     print(len(i))

# if len(mainlist) < 30:

#slice the list element down to 30 signs
# add ... instead
# around each item print a square

# (f"|{i}|").ljust(8)
# ("|masterpiece|").ljust(8)
# "|masterpiece|"
# for i in mainlist:
#     ("+"+ len(item1)*"-" + "+")