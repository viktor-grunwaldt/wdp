import math
def kolo(n:int) -> list[str]:
    img = []
    d = 2*n +1
    for i in range(1,d-2):
        row = ''
        for j in range(1,d-2):
            row += '#' if (i-n)**2 + (j-n)**2 < (n-1)**2 \
                    else ' '
        img.append(row)
        
    return img
    
    
def bauwan(a:int,b:int):
    for i in range(a,b):
        k = kolo(i)
        
        for line in k:
            if '#' in line:
                print(' '*(b-i) + line)
            
bauwan(5,8)
