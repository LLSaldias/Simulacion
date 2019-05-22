import random
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

#Test de Corridas para 10.000 rnd()
#----------------------------------

nrosAleatorios = []
secuencias = []
r = []
n = 10000
#n presente en ejemplo 6.7 de Kelton para validar cálculos
#n = 65536
nroClases = 5
sec = 1
chi = 0

aux = 0

#Generamos valores aleatorios
#----------------------------
for i in range (n):
    nrosAleatorios.append(random.random())
temp = nrosAleatorios[0]

#Contabilizamos secuencias
#-------------------------

for i in range (1,n):
    #print(i)
    if (nrosAleatorios[i] > temp):
        sec += 1
        #print(nrosAleatorios[i] > temp)
        temp = nrosAleatorios[i]
        if (i==n):
            secuencias.append(sec)
    else:
        secuencias.append(sec)
        sec = 1
        #print(nrosAleatorios[i] > temp)
        temp = nrosAleatorios[i]


#Contabilizamos fr de cada secuencia
#-----------------------------------

for j in range (0, 5):
    r.append(secuencias.count(j+1))
sum = 0
for j in range(5,10):
    #print(secuencias.count(j+1))
    sum = secuencias.count(j+1) + sum
r.append(sum)

#r presente en ejemplo 6.7 de Kelton para validar cálculos
#r = [10864,13695,5884,1778,401,84]
#print("Aleatorios",nrosAleatorios)
#print("secuencias fa", secuencias)
print("Secuencuas fr", r)
#print("Secuencias 6", secuencias.count(6))
#print("Secuencias 7", secuencias.count(7))
#print("Secuencias 8", secuencias.count(8))
#print("Secuencias 9", secuencias.count(9))

#Cálculo de variable Chi-cuadrado R
#----------------------------------

a= [ [ 4529.4,  9044.9, 13568.0, 18091.0, 22615.0, 27892.0],
[ 9044.9, 18097.0, 27139.0, 36187.0, 45234.0, 55789.0],
[13568.0, 27139.0, 40721.0, 54281.0, 67852.0, 83685.0],
[18091.0, 36187.0, 54281.0, 72414.0, 90470.0,111580.0],
[22615.0, 45234.0, 67852.0, 90470.0,113262.0,139476.0],
[27892.0, 55789.0, 83685.0,111580.0,139476.0,172860.0] ]
b= [ 1.0/6.0, 5.0/24.0, 11.0/120.0, 19.0/720.0, 29.0/5040.0, 1.0/840.0 ]

chi = 0
for i in range(0,6):
    for j in range(0,6):
        chi += (r[i] - n*b[i])*(r[j]-n*b[j])*a[i][j]
        #print("Ij", i,j)
chi = chi/n
print("R calculado:", chi)

#Desigualdad para verificar/rechazar hipótesis nula
#--------------------------------------------------

chi6 = 12.6 #Test de chi con 6 grados de libertad y 95% de confianza
print("Chi con 6 grados de libertad y 95% de confianza:",chi6)
if (chi > chi6):
    print("Se rechaza hipótesis nula. Los números generados son dependientes.")
else:
    print("No se rechaza hipótesis nula. Los número generados son independientes. ")