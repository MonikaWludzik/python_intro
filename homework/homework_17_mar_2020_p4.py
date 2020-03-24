# Zadanie 2
# all columns equal
# width 30 / sliced and substitue with ...
# embedded list

mainlist = ['masterpiece', 'centipede', 'skull', 'rest']
smainlist = (sorted(mainlist, key=len,reverse = True)) #sorting the list by len
item1 = smainlist[0]

# toprow = []
# for i in mainlist:
# toprow.append("+"+ len(item1)*"-" + "+") appending items to the list

toprow = ["+"+ len(item1)*"-" + "+" for i in mainlist] #looping the new list

for i in mainlist:
    (f"| {i} |").ljust(len(item1)) #adjust to left using the longest item

middlerow = [(f"| {i} |").ljust(len(item1)) for i in mainlist]

# (f"|{i}|").ljust(8)
# ("|masterpiece|").ljust(8)
# "|masterpiece|"
# for i in mainlist:
#     ("+"+ len(item1)*"-" + "+")

print(" ".join(toprow)) #join statement to print string for each item on the list
print(' '.join(middlerow))
print(" ".join(toprow))


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