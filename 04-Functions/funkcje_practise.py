def ile_liter(x):
    string = str(input('Podaj zdanie '))   
    licznik = 0
    x = str(x)
    for char in string:
        if char == x:
            licznik = licznik + 1
        else:
            licznik = licznik
    print(f"w zdaniu {string} jest {licznik} liter {x}")

#if __name__ == "__main__":
    #ile_liter('e')

def is_in_range(x,y):
    liczba = input('podaj liczbę ')
    liczba = int(liczba)

    for i in range(x,y + 1):
        if i == liczba:
            jest = True
            break
        else:
            jest = False 
    return jest

#ulansko = is_in_range(3,10)
#print(ulansko)

def hide(card_number):
    card_number = str(card_number)
    card = ''
    licznik = 0
    for char in card_number:
        licznik = licznik  +  1 
        if licznik > 2 and licznik < 13:
            char = '*'
        card = card + char 
    return card 

#ulansko = hide(2675847635678764)
#print(ulansko)






    
