zdanie = str(input('Podaj słowo do zaszyfrowania '))
zdanie_zasz = ''

for char in zdanie:
    if char == ' ':
        c = ' '
    elif char == 'a' or 'c' or 'z' or 't':
        a = ord(char)
        b = a + 8
        c = chr(b)    
    else:
        a = ord(char)
        b = a + 3 
        c =  chr(b)

    zdanie_zasz = zdanie_zasz + c 

print(zdanie_zasz)