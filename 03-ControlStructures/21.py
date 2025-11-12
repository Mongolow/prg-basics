number = int(input('Podaj kwotę '))
while number > 0:
    liczba_5 = number // 5
    reszta = number % 5 
    liczba_2 = reszta // 2
    reszta = liczba_2 % 2
    liczba_1 = reszta / 1
    number = 0

print(f'potrzeba {liczba_5} piątek {liczba_2} dwójek i {reszta} jedynek')
