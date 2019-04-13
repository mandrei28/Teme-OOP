from tema13 import *
#Marcu Andrei Cristian CEN 2.2A , problema nr 13

print('''Apasati tasta 1 pentru a initializa sistemul de cuburi
Apasati tasta 2 pentru a initializa lista de coordonate
Apasati tasta 3 pentru a afisa masa initializata anterior
Apasati tasta 4 pentru a afisa lista de coordonate initializate anterior
Apasati tasta 5 pentru a verifica daca exista drum intre coordonatele create anterior
Apasati tasta 6 pentru a verifica daca masa este in echilibru(greutatea in partea stanga este egala cu greutatea in partea dreapta)
Apasati tasta 7 pentru a afisa din nou meniul
Apasati orice tasta in afara de cele prezente in meniu pentru a opri executia programului
''')


while 1:

    command = input("Tasta:")

    if command == '1':

        Latime = int(input("Latimea mesei="))
        Lungime = int(input("Lungimea mesei="))
        Inaltime = int(input("Inaltime maxima="))
        NrCuburi = int(input("Numarul de cuburi="))
        Matrix = Masa(Latime,Lungime,NrCuburi,Inaltime)

    elif command == '2':

        NrCoordonate = int(input("Numar de perechi de coordonate:"))
        Coord = Coords(NrCoordonate)

    elif command == '3':

        Matrix.print_matrix()

    elif command == '4':

        Coord.print_coords()

    elif command == '5':

        for it1 in range(NrCoordonate):
            if Matrix.bfs(Coord.Coords[it1][0],Coord.Coords[it1][1],Coord.Coords[it1][2],Coord.Coords[it1][3]): 
                print(f"Exista drum intre punctele {Coord.Coords[it1][0]} , {Coord.Coords[it1][1]} si {Coord.Coords[it1][2]} , {Coord.Coords[it1][3]} ")
            else:
                print(f"Nu exista drum intre punctele {Coord.Coords[it1][0]} , {Coord.Coords[it1][1]} si {Coord.Coords[it1][2]} , {Coord.Coords[it1][3]} ")

    elif command == '6':

        Matrix.check_balance()

    elif command == '7':

        print('''Apasati tasta 1 pentru a initializa sistemul de cuburi
Apasati tasta 2 pentru a initializa lista de coordonate
Apasati tasta 3 pentru a afisa masa initializata anterior
Apasati tasta 4 pentru a afisa lista de coordonate initializate anterior
Apasati tasta 5 pentru a verifica daca exista drum intre coordonatele create anterior
Apasati tasta 6 pentru a verifica daca masa este in echilibru(greutatea in partea stanga este egala cu greutatea in partea dreapta)
Apasati tasta 7 pentru a afisa din nou meniul
Apasati orice tasta in afara de cele prezente in meniu pentru a opri executia programului
''')

    elif command != '7' and command != '6' and command != '5' and command != '4' and command != '3' and command != '2' and command != '1':
        break
