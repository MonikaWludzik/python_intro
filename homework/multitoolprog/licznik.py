def licznik():

    with open ('statystyki', 'r+') as stats:
        ilosc = list(stats.readlines())
        ilosc_u = 0
        if len(ilosc) > 1:
            ilosc_u = int(ilosc[1])


licznik()