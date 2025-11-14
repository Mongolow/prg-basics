def suma_znaków(a):
    a = int(a)
    liczba = abs(a)
    string = str(liczba)

    suma = 0
    for char in string:
        suma = suma + int(char)

    return suma

dana = input('podaj liczbe ')
print(suma_znaków(dana))

