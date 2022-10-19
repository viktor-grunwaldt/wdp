# rozm DLC = 5x5
from duze_cyfry import daj_cyfre
def dlc(n:int) -> str:
    num = str(n)
    l = len(num)
    img=""
    for i in range(5):
        for j in range(5*l):
            img+=daj_cyfre(int(num[j//5]))[i][j%5]
        img+='\n'    
        
    return img
    
print(dlc(123), end='')