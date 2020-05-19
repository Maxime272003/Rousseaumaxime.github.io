import random
import time
from matplotlib.pyplot import * 
maxVal = 2000
nVal = 10
listeNombres = random.choices(range(maxVal),k=nVal)

def rechercheNaive(L: list, elt: int)-> int:
    i = 0 
    for element in L : 
        if element == elt :
            return i 
        i += 1    
    return -1       


def rechercheDicho(L: list, elt: int)-> int:
    tr = False 
    deb = 0
    cnt = 0
    fin = len(L)-1
    while tr == False and deb <= fin : 
        mil = int((deb + fin) /2)
        if L[mil] == elt :
            tr = True 
            cnt = 1
        elif elt > L[mil] : 
            deb = mil + 1 
            cnt += 1
        else : 
            fin = mil - 1
            cnt += 1
    return tr, cnt

#print(rechercheNaive(listeNombres,4))
#print(rechercheDicho(listeNombres,9))

valeursX = [10,100,1000,10000,100000]
tDicho = []
tNaive = []
for nVal in valeursX :
    listeNombres = sorted(random.choices(range(maxVal),k=nVal))
    t1 = time.time()
    rechercheNaive(listeNombres, -1)
    t2 = time.time()
    tNaive.append(t2-t1)
    
    listeNombres = sorted(random.choices(range(maxVal),k=nVal))
    t1 = time.time()
    rechercheDicho(listeNombres, -1)
    t2 = time.time()
    tDicho.append(t2-t1)

print(tDicho)
print(tNaive)

loglog(valeursX, tNaive, '-xb')
loglog(valeursX, tDicho, '--+r')
show()
