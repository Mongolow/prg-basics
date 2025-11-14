
lista2 = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piatek']

def liczba_dzień(a):
    a = int(a)
    b = lista2[a - 1]

    return b

dana = input('podaj numer ')
print(liczba_dzień(dana))

