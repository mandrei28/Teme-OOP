from polinoame_coef import *


print('''Apasati tasta 1 pentru a crea o matrice de polinoame de la tastatura
Apasati tasta 2 pentru a crea o matrice de polinoame random
Apasati tasta 3 pentru a afisa matricea creata cu tasta 1 sau 2
Apasati tasta 4 pentru a calcula suma dintre doua matrici introduse de la tastatura
Apasati tasta 5 pentru a calcula suma dintre doua matrici generate random
Apasati tasta 6 pentru a calcula inmultirea dintre doua matrici introduse de la tastatura
Apasati tasta 7 pentru a calcula inmultirea dintre doua matrici generate random
Apasati tasta 8 pentru a evalua o matrice citita de la tastatura intr-un punct dat
Apasati tasta 9 pentru a evalua o matrice random intr-un punct dat
Apasati tasta 10 pentru a afisa din nou meniul
Apasati orice tasta in afara de cele prezente in meniu pentru a opri executia programului''')


while 1:

    command = input("Tasta:")

    if command == '1':

        n = int(input("Dimensiunea matricei="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        Matrix = input_matrix(n, max_grad_polinom)

    elif command == '2':

        n = int(input("Dimensiunea matricei="))
        max_coef = int(input("Coeficientul maxim al polinoamelor="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        Matrix = create_matrix(n, max_coef, max_grad_polinom)

    elif command == '3':

        print_matrix(Matrix)

    elif command == '4':

        n = int(input("Dimensiunea matricei="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        A = input_matrix(n, max_grad_polinom)
        B = input_matrix(n, max_grad_polinom)
        C = sum(A, B)
        print_matrix(A)
        print("+")
        print_matrix(B)
        print("=")
        print_matrix(C)
        print("\n")

    elif command == '5':

        n = int(input("Dimensiunea matricei="))
        max_coef = int(input("Coeficientul maxim al polinoamelor="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        A = create_matrix(n, max_coef, max_grad_polinom)
        B = create_matrix(n, max_coef, max_grad_polinom)
        C = sum(A, B)
        print_matrix(A)
        print("+")
        print_matrix(B)
        print("=")
        print_matrix(C)
        print("\n")

    elif command == '6':

        n = int(input("Dimensiunea matricei="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        A = input_matrix(n, max_grad_polinom)
        B = input_matrix(n, max_grad_polinom)
        C = prod(A, B)
        print_matrix(A)
        print("+")
        print_matrix(B)
        print("=")
        print_matrix(C)
        print("\n")

    elif command == '7':

        n = int(input("Dimensiunea matricei="))
        max_coef = int(input("Coeficientul maxim al polinoamelor="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        A = create_matrix(n, max_coef, max_grad_polinom)
        B = create_matrix(n, max_coef, max_grad_polinom)
        C = prod(A, B)
        print_matrix(A)
        print("+")
        print_matrix(B)
        print("=")
        print_matrix(C)
        print("\n")

    elif command == '8':

        n = int(input("Dimensiunea matricei="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        Matrix = input_matrix(n, max_grad_polinom)
        r = int(input('Radacina='))
        lin = int(input('Linia pe care se afla polinomul(matricea este indexata de la 0)='))
        col = int(input('Coloana pe care se afla polinomul(matricea este indexata de la 0)='))
        if lin <= n-1 and col <= n-1:
            Pij(r, lin, col, Matrix)
            print_matrix(Matrix)
        elif lin > n-1 and col > n-1:
            print("Linia si coloana au depasit dimensiunea declarata anterior!")
        elif lin > n-1:
            print("Linia a depasit dimensiunea declarata anterior!")
        elif col > n-1:
            print("Coloana a depasit dimensiunea declarata anterior!")

    elif command == '9':

        n = int(input("Dimensiunea matricei="))
        max_coef = int(input("Coeficientul maxim al polinoamelor="))
        max_grad_polinom = int(input("Gradul maxim al polinoamelor="))
        Matrix = create_matrix(n, max_coef, max_grad_polinom)
        r = int(input('Radacina='))
        lin = int(input('Linia pe care se afla polinomul(matricea este indexata de la 0)='))
        col = int(input('Coloana pe care se afla polinomul(matricea este indexata de la 0)='))
        if lin <= n-1 and col <= n-1:
            Pij(r, lin, col, Matrix)
            print_matrix(Matrix)
        elif lin > n-1 and col > n-1:
            print("Linia si coloana au depasit dimensiunea declarata anterior!")
        elif lin > n-1:
            print("Linia a depasit dimensiunea declarata anterior!")
        elif col > n-1:
            print("Coloana a depasit dimensiunea declarata anterior!")

    elif command == '10':

        print('''Apasati tasta 1 pentru a crea o matrice de polinoame de la tastatura
Apasati tasta 2 pentru a crea o matrice de polinoame random
Apasati tasta 3 pentru a afisa matricea creata cu tasta 1 sau 2
Apasati tasta 4 pentru a calcula suma dintre doua matrici introduse de la tastatura
Apasati tasta 5 pentru a calcula suma dintre doua matrici generate random
Apasati tasta 6 pentru a calcula inmultirea dintre doua matrici introduse de la tastatura
Apasati tasta 7 pentru a calcula inmultirea dintre doua matrici generate random
Apasati tasta 8 pentru a evalua o matrice citita de la tastatura intr-un punct dat
Apasati tasta 9 pentru a evalua o matrice random intr-un punct dat
Apasati tasta 10 pentru a afisa din nou meniul
Apasati orice tasta in afara de cele prezente in meniu pentru a opri executia programului''')

    elif command != '10' and command != '9' and command != '8' and command != '7' and command != '6' and command != '5' and command != '4' and command != '3' and command != '2' and command != '1':
        break