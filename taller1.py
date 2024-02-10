#Brayan Steven León Martinez - Taller 1 - Matemáticas Computacional"

cantidad_a = int(input('Ingrese la cantidad del grupo A: '))

a = set()
for i in range(cantidad_a):
    elementoA = float(input('Elemento ' + str(i+1) + ':'))
    a.add(elementoA)

print(a)

cantidad_b = int(input('Ingrese la cantidad del grupo B: '))

b = set()
for l in range(cantidad_b):
    elementoB = float(input('Elemento ' + str(l+1) + ':'))
    b.add(elementoB)

print(b)

r = set()

option = int(input(''' 
Menú:
1. Unión
2. Intersección
3. Diferencia
4. Diferencia Simétrica
Eliga una de las opciones anteriores: '''))
if option == 1:
  r = a|b
  print("Unión:")
  print(r)
elif option == 2:
  r = a&b
  print("Intersección:")
  print(r)
elif option == 3:
  r = a-b
  print("Diferencia A con B:")
  print(r)
  r = b-a
  print("Diferencia B con A:")
  print(r)
elif option == 4:
  r = a^b
  print("Diferencia Simétrica:")
  print(r)
else:
  print("Por favor seleccionar una opción válida")
