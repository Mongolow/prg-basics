import math

def triangle_area(a,b,c):
    p = (a + b + c) / 2
    result = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return result 

pole = triangle_area(3,4,5)
print(pole)