def leapyear(leap):
    if(leap > 0):
        if (leap % 4) == 0:
            if (leap % 100) == 0:
                if (leap % 400) == 0:
                    print("\t{0} szökőév".format(leap))
                else:
                    print("\t{0} nem szökőév".format(leap))
            else:
                print("\t{0} szökőév".format(leap))
        else:
            print("\t{0} nem szökőév".format(leap))
    else:
        leap = int(input("\tKérek egy évszámot: "))
        return leapyear(leap)