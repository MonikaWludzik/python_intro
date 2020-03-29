import textstat as textstat

textstat.set_lang("en")

def get_digits(contents):
    c = ""
    for i in contents:
        if i.isdigit():
            c += i
    return c

def get_lower_case(contents):
    c= ""
    for i in contents:
        if i.islower():
            c += i
    return c

with open ('plik_do_odczytu', 'r+') as plik:
    contents = plik.read()
    print(contents)
    print(textstat.char_count(contents)) #characters in the file
    print(textstat.lexicon_count(contents, removepunct=True)) #wordcount
    print(textstat.sentence_count(contents)) #sentencecount
    print(get_digits(contents))
    print(get_lower_case(contents))








#     try:
#         ilosc_uruchomien = int(ilosc_uruchomien)
#         ilosc_uruchomien = ilosc_uruchomien =+ 1
#     except:
#         ilosc_uruchomien = 1
#     print(ilosc_uruchomien)
#
#
#




# 1) open file
# 2) count
#
# a) number of times the file was opened

# d) digits
# e) small letters
# f) stats

# saveit