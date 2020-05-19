
# --- DEFINITION DES FONCTIONS ---

def hexaDigits( n: int) -> str :
    symbolHexa = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    #symbolHexa = [str(i) for i in range(10)]
    #symbolHexa.extend(['a','b','c','d','e','f'])
    return symbolHexa[n]

def isBin2( n: int ) -> bool :
    # version optimisée de isBin
    nStr = str(n)
    for i in nStr:
        if i != '0' and i != '1': return False
    return True

def isBin( n: int ) -> bool :
    # version demandée de isBin
    nStr = str(n)
    test = True
    for i in nStr:
        if i != '0' and i != '1': test = False
    else: test = True
    return test

def fillBits(n: int) -> int :
    # % 8 permet d'avoir un octet (8 bits)
    n = str(n)
    L = len(n)
    while L % 8 != 0:
        n =  '0' +n
        L = len(n)
    return n

def bin2dec( n: int ) -> int :
    # prenez garde aux types utilisés (i est un string que l'on convertit en int)
    nStr = str(n)
    L = len(nStr)-1
    d = 0
    for i in nStr:
        d = d + int(i)*2.0**L
        L = L - 1
    return int(d)

def dec2bin( n: int ) -> str :
    #a = b x q+r
    reste = ''
    a = n
    while a != 0:
        reste = str(a%2) + reste
        a = a // 2
    return reste

def dec2hexa( n: int ) -> str :
    if n == 0: return  str(0)
    reste = ''
    a = n
    while a != 0:
        # hexaDigits(a%16) permet de convertir un nombre entre 0 et 15 en
        # symboles hexa entre 0 et F. str n'est pas obligatoire mais peut
        # éviter les problèmes inattendus !
        reste = str(hexaDigits(a%16)) + reste
        a = a // 16
    return reste

def bin2hexa(n: int) -> str :
    # on met le binaire n sur 8 bits avec fillBits()
    nStr = str(fillBits(n))
    L = len(nStr)
    nHexa = ''
    # on lit les bits 4 par 4 à l'aide de nStr[i:i+4]
    # on convertit en decimal à l'aide de bin2dec()
    # on convertit le nombre entre 0 et 15 avec hexaDigits()
    for i in range(0,L,4):
        nHexa = nHexa + str(hexaDigits(bin2dec(nStr[i:i+4])))
    return nHexa

def bin2hexa2(n: int) -> str :
    # version courte : on convertit n de binaire à base 10 puis on convertit
    # de base 10 à hexa...
    return dec2hexa(bin2dec(n))



# --- PROGRAMME PRINCIPAL : quelques tests ---


print( bin2hexa(11011), bin2hexa2(11011) )

#print(fillBits(10011))
print(dec2hexa(bin2dec(10001)))
print(dec2bin(25),bin(25))
#print(bin2hexa(110110101))
#print(isBin(12001))
print(hexaDigits(12))
print(dec2hexa(156),hex(156))

print(' ', [str(j).rjust(4) for j in range(6)])
for i in range(10):
    print(i, [dec2hexa(i+j*10).rjust(4) for j in range(6)])
