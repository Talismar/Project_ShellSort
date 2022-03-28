import os
import random
import time

cont = 0
def shellshort(lista, tam=None):
    global cont
    if tam == None:
        tam = len(lista)
    
    "Distancia"
    h = tam//2

    "Quebrando as distancias - Diferenca do insertion sort é a distancia - Dessa forma quando o h for igual a 1 é o mesmo algoritmo que o insertion sort"
    while h > 0:
        i = h
        while i < tam: 
            aux = lista[i]             
            j = i                      
            while j >= h and aux < lista[j-h]: 
                lista[j]= lista[j-h]
                cont+=1
                j = j - h
                #print(aux,"-",lista[j-h])
            lista[j] = aux
            i+=1
        h = h//2

#n * n/2

os.system("clear")
A = []
 
for i in range(0,1000000):
    A.append(random.randint(0,100)) 

"Lista desordenada"
print("Lista desordenada > ",A)

"Calculando o tempo"
start = time.time()
shellshort(A)
end = time.time()

"Lista ordenada"
print(A)

"Resultado do tempo"
print("Time - Shell Sort: ", round(end-start,8))

print("Trocas ", cont) 