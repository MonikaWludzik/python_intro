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
    # print(contents)
    # print(textstat.char_count(contents)) #characters in the file
    # print(textstat.lexicon_count(contents, removepunct=True)) #wordcount
    # print(textstat.sentence_count(contents)) #sentencecount
    # print(get_digits(contents))
    # print(len(get_lower_case(contents)))

    with open ('statystyki', 'r+') as stats:
        ilosc = list(stats.readlines())
        ilosc_u = 0
        if len(ilosc) > 1:
            ilosc_u = int(ilosc[1])
        stats.truncate(0)
        stats.seek(0)
        stats.write('Ilosc uruchomien: \n'+ (str(ilosc_u+1)+"\n"))
        stats.write("Ilosc znakow: \n"+(str(textstat.char_count(contents))+"\n"))
        stats.write("Ilosc slow: \n"+ str(textstat.lexicon_count(contents, removepunct=True))+"\n")
        stats.write("Ilosc zdan: \n"+ str(textstat.sentence_count(contents))+"\n")
        stats.write("Ilosc cyfr: \n"+str(get_digits(contents))+"\n")
        stats.write("Ilosc malych liter: \n"+str(len(get_lower_case(contents)))+"\n")


