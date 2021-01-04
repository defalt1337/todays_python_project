def evszamok(year):
    if year < 0:
        ##year = int(input("\tKérek egy évszámot: "))
        return evszamok(year)
    else:
        years = int(year/100+1)
        print("\tAz", year, "a(z)",years, ". században található! ")