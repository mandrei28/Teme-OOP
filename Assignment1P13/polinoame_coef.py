from random import randint

def input_matrix(no_Of_Elements, max_grad_polinom):#crearea matricei patratate de polinoame de la tastatura
    Matrix = [] 
    for it1 in range(no_Of_Elements):
        row = [] 
        for it2 in range(no_Of_Elements):
            polinom = []  
            print(f'Polinomul situat pe linia {it1} coloana {it2} :' , end=" ")
            for it3 in range(max_grad_polinom+1):
                print(f'Coeficientul lui x^{it3}=', end="")
                polinom.append(int(input())) #adaugam in vectorul polinom coeficientii cititi de la tastatura(polinom[0] fiind coeficientul lui x^0, polinom[1] coeficientul lui x^1...)
            row.append(polinom) #adaugam in vectorul row polinomul creat anterior
        Matrix.append(row) #adaugam in vectorul Matrix randul de polinoame creat anterior formand astfel o matrice tridimensionala
    return Matrix

def create_matrix(no_Of_Elements, max_coef, max_grad_polinom): #crearea matricei patrate de polinoame generate random
    Matrix = [] 
    for it1 in range(no_Of_Elements):
        row = [] 
        for it2 in range(no_Of_Elements):
            polinom = [] 
            for it3 in range(max_grad_polinom+1):
                polinom.append(randint(0, max_coef)) #adaugam in vectorul polinom un numar random generat intre 0 si variabila max_coef(polinom[0] fiind coeficientul lui x^0, polinom[1] coeficientul lui x^1...)
            row.append(polinom) #adaugam in vectorul row polinomul creat anterior
        Matrix.append(row) #adaugam in vectorul Matrix randul de polinoame creat anterior formand astfel o matrice tridimensionala
    return Matrix
 
def print_matrix(Matrix): #afisarea matricei patrate de polinoame cu coeficienti reali
    for it1 in range(len(Matrix)):
        for it2 in range(len(Matrix[it1])):
            print(f'Polinomul situat pe linia {it1} coloana {it2} este:', end=" ")
            for it3 in range(len(Matrix[it1][it2])):
                print(f'{Matrix[it1][it2][it3]}*x^{it3}', end="")
                if it3 != (len(Matrix[it1][it2])-1):
                    print('+', end="")
            print('\n', end="")
 
def Pij(root, position1, position2, Matrix): #evaluarea unui polinom intr-un punct dat p
    value = 0
    polinom = Matrix[position1][position2]
    for it1 in range(len(polinom)):
        value = value + polinom[it1] * (root ** it1) #calculam polinomul inlocuind x-ul cu root
    print(f'Valoarea polinomului situat pe linia {position1} coloana {position2} in punctul {root} este: {value}')
 
def sum(A, B): #suma a doua matrici A si B
    Matrix = []
    for it1 in range(len(A)):
        row = []
        for it2 in range(len(A[it1])):
            polinom = []
            for it3 in range(len(A[it1][it2])):
                polinom.append(A[it1][it2][it3] + B[it1][it2][it3]) #adunam cele doua polinoame coeficient cu coeficient si le stocam in vectorul polinom
            row.append(polinom)
        Matrix.append(row)
    return Matrix

def prodpol(A, B): #produsul dintre doua polinoame A si B
    polinom = [0]*(len(A)+len(B))
    for it1 in range(len(A)):
        for it2 in range(len(B)):
            polinom[it1+it2] += A[it1]*B[it2]
    return polinom

def sumpol(vector_of_poli): #suma polinoamelor aflate intr-un vector
    sum = [0]*(len(vector_of_poli[0]))
    for it1 in range(len(vector_of_poli)):
        for it2 in range(len(vector_of_poli[it1])):
            sum [it2] += vector_of_poli[it1][it2]
    return sum

def prod(A, B): #produsul intre doua matrici A si B
    Matrix = []
    for it1 in range(len(A)):
        row = []
        for it2 in range(len(A)):
            polinom = []
            for it3 in range(len(A)):
                polinom.append(prodpol(A[it1][it3],B[it3][it2])) #calculam produsul dintre polinomul A si polinomul B folosind functia prodpol
            row.append(sumpol(polinom)) #vectorul polinom contine len(A) polinoame, realizam suma acestora folosind functia sumpol pentru a obtine polinomul final
        Matrix.append(row)
    return Matrix
