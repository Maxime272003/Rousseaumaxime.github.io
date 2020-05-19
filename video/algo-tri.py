import time
import random

maxVal = 10
nVal = 5
listeNombres = random.choices(range(maxVal),k=nVal)

def triSelection(L: list)-> list:
	cnt = 0
	n = len(L)
	for i in range(0, n-1) :
		indiceMini = i
		for j in range(i, n) :
			cnt +=1
			if L[j] < L[indiceMini] :
				indiceMini = j
			temp = L[i]
			#print('avant', L)
			L[i] = L[indiceMini]
			L[indiceMini] = temp
			#print('après', L)
	return L, cnt


def triInsertion(L: list)-> list:
	n = len(L)
	cnt = 0
	for i in range(1,n) :
		valeurTraitee = L[i]
		j = i - 1
		while j >= 0 and valeurTraitee < L[j] :
			L[j+1] = L[j]
			cnt += 1
			j = j - 1
		cnt += 1
		L[j+1] = valeurTraitee
	return L, cnt


#listeNombresTriee = triSelection(listeNombres) # trie la liste
#print(listeNombresTriee) # affiche la liste

#print(triInsertion(listeNombres))


valeursX = [10,100,1000,10000,100000]
tSelection = []
tInter = []

for nVal in valeursX :
    listeNombres = random.choices(range(maxVal),k=nVal)
    t1 = time.time()
    triSelection(listeNombres)
    t2 = time.time()
    tSelection.append(t2-t1)

    t1 = time.time()
    triInsertion(listeNombres)
    t2 = time.time()
    tInter.append(t2-t1)

print(tSelection)
print(tInter)
