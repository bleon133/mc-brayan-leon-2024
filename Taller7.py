#Brayan Steven León Martinez - Taller 7 - Matemáticas Computacional
import math

x = 0.75
es = (0.5 * (10**-8))*100
ea = 100
valor = 1
iteraciones = 1

while ea > es:
    valor_ant = valor
    
    if(iteraciones % 2 == 0):
        valor = valor_ant + (x)**iteraciones / math.factorial(iteraciones)
    else:
        valor = valor_ant - (x)**iteraciones / math.factorial(iteraciones)
        
    ea = abs((valor - valor_ant) / valor) * 100
    
    iteraciones += 1

# Resultados 1
print("Valor Estimado Caso 1: ", valor)
print("Error Aproximado Caso 1: ", ea)
print("Error aproximado relativo porcentual Caso 1: ", es)
print("Número iteraciones Caso 1: ",iteraciones)

ea = 100
valor2 = 0  
iteraciones2 = 0  

while ea > es:
    valor_ant_ex = valor2
    
    valor2 = valor2 + x**iteraciones2 / math.factorial(iteraciones2)
        
    if iteraciones2 > 0:
        ea = abs((valor2 - valor_ant_ex) / valor2) * 100
    
    iteraciones2 += 1

valor2 = 1 / valor2

# Resultados 2
print("Valor Estimado Caso 2: ", valor2)
print("Error Aproximado Caso 2: ", ea)
print("Error aproximado relativo porcentual Caso 2: ", es)
print("Número iteraciones Caso 2: ",iteraciones2)
