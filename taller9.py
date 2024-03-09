#Brayan Steven León Martinez - Taller 6 - Matemáticas Computacional
import math

x = float(input("Ingrese un valor del ángulo en radianes: "))
print(x)
es = (0.5 * (10**-8))*100

ea = 100
valor = 1
iteraciones = 1
factorialNum = 1
while ea > es:
    valor_ant = valor

    if(iteraciones == 1):
        valor = x
    else:
        if(iteraciones % 2 == 0):
            valor = valor_ant - x**factorialNum/math.factorial(factorialNum)
        else:
            valor = valor_ant + x**factorialNum/math.factorial(factorialNum)

    if(iteraciones > 1):
        ea = abs((valor - valor_ant) / valor) * 100
    print(iteraciones)
    iteraciones += 1
    factorialNum +=2


print("Valor Estimado: ", valor)
print("Error Aproximado: ", ea)
print("Error aproximado relativo porcentual: ", es)
print("Número iteraciones: ",iteraciones)
