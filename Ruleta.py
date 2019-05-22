import random
import matplotlib.pyplot as plt

numero = int(input("Numero elegido:"))

iteracion = input("Cantidad de iteraciones:")
esp = float(1)/37
media_t=0
varianza_t=0
n = 37
fr_abs = []
media_real=[]
varianza=[]
muestra = []
ejex = []
fr_rel = []

print("Ruleta!")

def varianza_func(lista, media):
  s = 0
  for elemento in lista:
    s += (elemento - media) ** 2
  return s / float(len(lista))

# inicializo arreglos y calculo media teorica (18)
for x in range(0, n):
    media_t += float(esp*x)

# varianza teorica (104)
for x in range(0, n):
    varianza_t += ((x - media_t)**2)*esp

#Armado de muestra
for x in range(0, int(iteracion)):
    rand = random.randint(0, 36)
    muestra.append(rand)
    fr_rel.append(float(muestra.count(numero)) / (x+1))
    media_real.append(float(sum(muestra)) / (x+1))
    varianza.append(varianza_func(muestra, media_real[x]))

# grafico media teorica
plt.figure(1)
plt.xlabel('Tiradas')
plt.ylabel('Media')
plt.title('Media')
plt.axhline(media_t, 0, iteracion)
plt.plot(media_real, 'g')

#grafico varianza teorica
plt.figure(2)
plt.xlabel('Tiradas')
plt.ylabel('Varianza')
plt.title('Varianza')
plt.axhline(varianza_t,0, iteracion)
plt.plot(varianza, 'y')

#grafico varianza teorica
plt.figure(3)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.title('Frecuencia relativa del numero: ' + str(numero))
plt.axhline(esp, 0, iteracion)
plt.plot(fr_rel, 'r')

plt.show()
