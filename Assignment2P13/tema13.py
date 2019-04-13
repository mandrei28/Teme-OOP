import queue

class Coords:
    def __init__(self, n_Of_Coords): # init lista de coordonate
        self.Coords = [[0 for it1 in range(4)] for it2 in range(n_Of_Coords)]
        self.n_Of_Coords = n_Of_Coords
        for it1 in range(n_Of_Coords):
            x1 = int(input("X-ul punctului de plecare:"))
            y1 = int(input("Y-ul punctului de plecare:"))
            x2 = int(input("X-ul punctului de sosire:"))
            y2 = int(input("Y-ul punctului de sosire:"))
            self.Coords[it1][0]=x1
            self.Coords[it1][1]=y1
            self.Coords[it1][2]=x2
            self.Coords[it1][3]=y2

    def print_coords(self): # afisare lista de coordonate
        for it1 in range(self.n_Of_Coords):
            print(f"x1 = {self.Coords[it1][0]} y1 = {self.Coords[it1][1]} x2 = {self.Coords[it1][2]} y2 = {self.Coords[it1][3]}")

            
class Masa:
    def __init__(self, n_Of_Rows, n_Of_Columns, n_Of_Cubes, max_Height): # initializare sistem de cuburi
        self.Matrix = [[[0 for it1 in range(max_Height)] for it2 in range(n_Of_Columns)] for it3 in range(n_Of_Rows)] # initializare cu 0 a sistemului de cuburi
        self.visited = [[0 for it1 in range(n_Of_Columns)] for it2 in range(n_Of_Rows)] # initializarea cu 0 a matricei visited utilizata ulterior la bfs
        self.n_Of_Rows = n_Of_Rows
        self.n_Of_Columns = n_Of_Columns
        self.n_Of_Cubes = n_Of_Cubes
        self.max_Height = max_Height
        print(f"Dimensiunea mesei este de {n_Of_Rows} x {n_Of_Columns}")
        print(f"X-ul este indexat de la 0 la {n_Of_Rows-1} si Y-ul este indexat de la 0 la {n_Of_Columns-1}")
        cubes = 0
        while cubes < n_Of_Cubes:
            x1 = int(input(f"X-ul punctului de plecare al cubului {cubes} :"))
            y1 = int(input(f"Y-ul punctului de plecare al cubului {cubes} :"))
            x2 = int(input(f"X-ul punctului de sosire al cubului {cubes} (cel mai indepartat punct aflat pe aceeasi diagonala cu punctul de pornire) :"))
            y2 = int(input(f"Y-ul punctului de sosire al cubului {cubes} (cel mai indepartat punct aflat pe aceeasi diagonala cu punctul de pornire) :"))
            #Metoda mea de initializare a fost urmatoarea: dau punctele extreme de pe o diagonala, de exemplu 1,1 si 2,2; De aici pot sa calculez inaltimea
            #care este abs(y2 - y1) + 1. Apoi parcurg elementele 11 12 21 22 si umplu pana la inaltimea calculata anterior daca am loc liber.
            #In cazul in care nu am loc liber urc in inaltime folosindu-ma de inaltimea calculata anterior

            height = abs(y2 - y1) # un cub are toate laturile egale, automat din moment ce stim marimea bazei acestuia putem sa calculam inaltimea scazand y-urile punctelor opuse
            if(x1 > x2): # interschimbam valorile pentru a ne fi mai usor de parcurs cand umplem matricea ( de la mic la mare )
                aux = x1
                x1 = x2
                x2 = aux
            if(y1 > y2): 
                aux = y1
                y1 = y2
                y2 = aux
            level = 0 # Variabila utilizata pentru a retine de la ce nivel pot incepe umplerea matricei(range-ul (level, level+height) are doar elemente 0)
            while 1:
                ok = 0
                for it1 in range(x1, x2 + 1): # parcurgem punctele de la mic la mare 
                    for it2 in range(y1, y2 + 1):
                        for it3 in range(level, level + height + 1): # parcurgem matricea in inaltime, folosim level pentru cazul in care este ocupat deja acel nivel si dorim sa retinem unde este liber
                            if(self.Matrix[it1][it2][it3] != 0):
                                ok = 1
                if ok == 0: # am gasit loc sa introducem cubul
                    break
                else:
                    level = level + height + 1 # incepem sa cautam mai sus deoarece nivelele verificate anterior erau ocupate de alt cub
                    if level + height + 1 > self.max_Height: # conditie in caz ca inaltimea declarata este prea mica
                        print("Cubul a depasit inaltimea maxima, rulati din nou programul")
                        break
            for it1 in range(x1, x2 + 1): # dupa ce am gasit loc in matrice ne folosim de level pentru a o umple cu 1 in locurile in care este un cub
                    for it2 in range(y1, y2 + 1):
                        for it3 in range(level, level + height + 1):
                            self.Matrix[it1][it2][it3] = 1
            cubes = cubes + 1 # contorul pt cuburi

    def print_matrix(self):
        print("0 reprezinta loc liber pe masa la inaltimea respectiva, 1 reprezinta prezenta o parte(sau chiar un cub cu 1x1x1)a unui cub la inaltimea respectiva")
        print("Linia de mai jos are scopul de a face citirea nivelelor mai usoara, indicand nivelul la care se alfa fiecare element de sub")
        for it1 in range(len(self.Matrix[0])):# Am afisat o lista de nivele pentru a fi mai usoara citirea matricei. Aceasta linie nu face parte din matrice !
            for it2 in range(len(self.Matrix[0][0])):
                print(it2, end=" ")
            print(end=" ")
        print("\nMatricea de cuburi:")#Afisarea matricei de cuburi, 0 fiind loc liber 1 fiind loc ocupat
        for it1 in range(len(self.Matrix)):
            for it2 in range(len(self.Matrix[0])):
                for it3 in range(len(self.Matrix[0][0])):
                    print(self.Matrix[it1][it2][it3], end=" ")
                print(" ", end="")
            print("\n")

    def isValid(self, row, col):#Verificare vecini matrice pentru bfs, daca functia returneaza 1 punctul este introdus in coada
        return row >= 0 and row < self.n_Of_Rows and col >=0 and col < self.n_Of_Columns and self.Matrix[row][col][0] == 0 and self.visited[row][col] == 0

    #Am folosit bfs pentru verificarea drumului(Algoritmul lui Lee)
    def bfs(self, x1, y1, x2, y2):
        if self.Matrix[x1][y1][0] == 1 or self.Matrix[x2][y2][0] == 1:
            print("Pe unul din coordonate se afla deja cub => nu exista drum")
            return 0
        row = [ -1, 0, 0, 1 ] #Vectori utili la verificarea vecinilor, pt a nu scrie de fiecare data -1, +1 etc.
        col = [ 0, -1, 1, 0 ] # "-"
        neighbours = queue.Queue(maxsize = 20) # Avem nevoie de o structura FIFO pentru bfs, am folosit queue. La fel de bine ar fi mers si cu o lista.
        self.visited[x1][y1] = 1; #Pastram nodurile vizitate pentru a nu parcurge de mai multe ori din acelasi punct.
        neighbours.put((x1, y1)) 
        while neighbours.empty() == 0:
            coord1, coord2 = neighbours.get() # Luam din coada primele coordonatele aflate sus si in acelasi timp le si eliminam din coada.
            if coord1 == x2 and coord2 == y2: # Am ajuns la destinatie, nu are rost sa mai parcurgem.
                break
            for it1 in range(4):#Verificam daca punctul unde am ajuns mai are vecini pe unde putem sa parcurgem in continuare.
                if self.isValid(coord1 + row[it1], coord2 + col[it1]):
                    self.visited[coord1 + row[it1]][coord2 + col[it1]] = 1 # Am gasit un vecin, il adaugam in visited.
                    neighbours.put((coord1 + row[it1], coord2 + col[it1])) # Adaugam vecinul in coada.
            neighbours.task_done()
        if self.visited[x2][y2] == 1:
            return 1 #Punctul a fost vizitat => exista drum de la sursa la destinatie.
        else:
            return 0 #Punctul nu a fost vizitat => nu exista drum de la sursa la destinatie.
    def check_balance(self):
        #Nu am inteles exact aceasta cerinta.
        #Am presupus ca un sistem este in echilibru daca masa are greutati egale in partea stanga si dreapta(fiind impartita in jumatati)
        countleft = 0
        countright = 0
        if self.n_Of_Columns % 2 != 0: #Exista 2 cazuri, cand avem numar impar de coloane si evitam coloana din mijloc si cazul in care avem numar par si luam toate coloanele
            #Acesta este cazul pentru numar de coloane par (n_Of_Columns - 1)
            for it1 in range(len(self.Matrix)):
                for it2 in range(len(self.Matrix[0])):
                    for it3 in range(len(self.Matrix[0][0])):
                        if it2 < (self.n_Of_Columns - 1) / 2 and self.Matrix[it1][it2][it3] == 1: #Ne aflam in partea stanga a mesei
                            countleft = countleft + 1
                        elif it2 > (self.n_Of_Columns - 1) / 2 and self.Matrix[it1][it2][it3] == 1: #Ne aflam in partea dreapta a mesei
                            countright = countright +1
            if countright == countleft: 
                print("Greutatea de pe partea stanga a mesei este egala cu greutatea din partea dreapta")
            elif countright > countleft: 
                print("Partea dreapta este mai grea decat partea stanga")
            elif countleft > countright:
                print("Partea stanga este mai grea decat partea dreapta")
        elif self.n_Of_Columns % 2 == 0: #Numarul de coloane este impar
            for it1 in range(len(self.Matrix)):
                for it2 in range(len(self.Matrix[0])):
                    for it3 in range(len(self.Matrix[0][0])):
                        if it2 <= (self.n_Of_Columns - 1) / 2 and self.Matrix[it1][it2][it3] == 1: #Ne aflam in partea stanga a mesei
                            countleft = countleft + 1
                        elif it2 > (self.n_Of_Columns - 1) / 2 and self.Matrix[it1][it2][it3] == 1: #Ne aflam in partea dreapta a mesei
                            countright = countright +1
            if countright == countleft:
                print("Greutatea de pe partea stanga a mesei este egala cu greutatea din partea dreapta")
            elif countright > countleft:
                print("Partea dreapta este mai grea decat partea stanga")
            elif countleft > countright:
                print("Partea stanga este mai grea decat partea dreapta")
