while True:
    number = int(input('Podaj liszbę w systemie dziesiętnym '))
    bin_rev = ''
    while number > 0:
        reszta = number % 2
        if reszta > 0:
            bin_rev = bin_rev + '1'
        else:
            bin_rev = bin_rev + '0'
        reszta = 0
        number = number // 2


    print(bin_rev[::-1])