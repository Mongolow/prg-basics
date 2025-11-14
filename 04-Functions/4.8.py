
def time_string(a,b,format):
    if format == '24':
        if b < 10:
            result = f"{a}:0{b}"
        else:
            result = f"{a}:{b}"
    else:
        if a > 12:
            if b < 10:
                result = f"{a - 12}:0{b}pm"
            else:
                result = f"{a - 12}:{b}pm"
        elif a == 12:
            if b < 10:
                result = f"{12}:0{b}pm"
            else:
                result = f"{12}:{b}pm"
        elif a == 0:
            if b < 10:
                result = f"{12}:0{b}am"
            else:
                result = f"{12}:{b}am"
        else:
            if  b < 10:
                result = f"{a}:0{b}am"
            else:
                result = f'{a}:{b}am'
    return result



print(time_string(15, 38, '24'))
print(time_string(8, 3, '24')) 
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12')) 
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12')) 
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))