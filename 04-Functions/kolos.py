def f(name):
    if name == '':
        akronim = ''
    else:
        akronim = name[0]
    znacznik = 0
    for char in name:
        if char == ' ':
            znacznik = 1
            continue
        if znacznik == 1:
            akronim = akronim + char 
            znacznik = 0
    return akronim 



if __name__ == '__main__':
    print(f('moja Mała jkl'))

        
         
