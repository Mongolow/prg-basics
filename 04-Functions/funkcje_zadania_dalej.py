def f(amount_to_pay):
    reszta = amount_to_pay % 5
    liczba_5 = amount_to_pay // 5
    liczba_2 = reszta // 2
    reszta = reszta % 2
    liczba_1 = reszta
    min_mon = liczba_5 + liczba_2 + liczba_1
    return min_mon

#if __name__ == '__main__':
    #print(f(8))

def f2(number,even):
    even = bool(even)
    number = str(number)
    if even:
        suma = 0
        for char in number:
            if int(char) % 2 == 0:
                suma = suma + int(char)
            else:
                continue
    else:
        suma = 0 
        for char in number:
            if not int(char) % 2 ==0:
                suma = suma + int(char)
            else:
                continue
    return suma 

#if __name__ == '__main__':
    #print(f2(13115,True))

def f3(x,y):
    suma = 0
    for i in range(x,y):
        if i % 2 == 0 and i < 0:
            suma = suma + 1
        else:
            continue
    return suma

#if __name__ == '__main__':
    #print(f3(-1,11))

def f4(n1,n2,n3):
    lista = [n1,n2,n3]
    for x in lista:
        if int(x) < 0:
            wynik = True
            break 
        else:
            wynik = False
    return wynik

#if __name__ == '__main__':
    #print(f4(3,6,14))

def f5(x):
    wynik = '*'
    for i in range(0,x-1):
        wynik = wynik + '/*'
    return wynik

if __name__ == '__main__':
    print(f5(20))



