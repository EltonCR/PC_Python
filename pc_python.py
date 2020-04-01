#pontos cartesiano
import math
x1 = int(input("Digite o valor inteiro de X1 para coordenada 1: "))
y1 = int(input("Digite o valor inteiro de Y1 para coordenada 1: "))
x2 = int(input("Digite o valor inteiro de X2 para coordenada 2: "))
y2 = int(input("Digite o valor inteiro de X2 para coordenada 2: "))

v = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if (v >= 10):

    print("distante")

else:

    print("próximo")