csillagjegyek = ["majom","kakas","kutya","disznó","patkány","bivaly","tigris","nyúl","sárkány","kígyó","ló","kecske"]
def kinaijegy(evszam):
    if(evszam > 0):
        if(evszam % 12) == 0:
            print("\tA te kínai csillagjegyed:",csillagjegyek[0])
        elif(evszam % 12) == 1:
            print("\tA te kínai csillagjegyed:",csillagjegyek[1])
        elif (evszam % 12) == 2:
            print("\tA te kínai csillagjegyed:",csillagjegyek[2])
        elif (evszam % 12) == 3:
            print("\tA te kínai csillagjegyed:",csillagjegyek[3])
        elif (evszam % 12) == 4:
            print("\tA te kínai csillagjegyed:",csillagjegyek[4])
        elif (evszam % 12) == 5:
            print("\tA te kínai csillagjegyed:",csillagjegyek[5])
        elif (evszam % 12) == 6:
            print("\tA te kínai csillagjegyed:",csillagjegyek[6])
        elif (evszam % 12) == 7:
            print("\tA te kínai csillagjegyed:",csillagjegyek[7])
        elif (evszam % 12) == 8:
            print("\tA te kínai csillagjegyed:",csillagjegyek[8])
        elif (evszam % 12) == 9:
            print("\tA te kínai csillagjegyed:",csillagjegyek[9])
        elif (evszam % 12) == 10:
            print("\tA te kínai csillagjegyed:",csillagjegyek[10])
        elif (evszam % 12) == 11:
            print("\tA te kínai csillagjegyed:",csillagjegyek[11])
    else:
        evszam = int(input("Add meg a születési éved: "))
        return kinaijegy(evszam)