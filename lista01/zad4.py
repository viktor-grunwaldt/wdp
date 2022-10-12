#znowu nie ma skosa ale tym razem mogę kombinować
from losowanie_fragmentow import losuj_fragment

# print(*(losuj_fragment() for _ in range(5)), sep='\n')

def losuj_haslo(n:int) -> str:
    assert n > 1
    #dp?
    haslo = ""
    # losujemy dopóki l < n-4 aby uniknąć sytuacji, gdzie l= n-1
    # (wtedy trzeba by bylo coś usuwać)
    while len(haslo) < n-5:
        frag = losuj_fragment()
        haslo += frag
    
    #pominięcie przypadku len(haslo) = n-1
    while len(haslo) == n-5:
        frag = losuj_fragment()
        if len(frag) < 4:
            haslo += frag
            break
    
    #szukamy ostatniego fragmentu]
    while len(haslo) < n:
        frag = losuj_fragment()
        if len(frag) == n-len(haslo):
            haslo += frag
            break
    
    return haslo

print(*(losuj_haslo(8) for _ in range(10)), sep='\n')
print(*(losuj_haslo(12) for _ in range(10)), sep='\n')
