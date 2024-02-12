#Brayan Steven León Martinez - Taller 2 - Matemáticas Computacional

cantidad_u = int(input("Ingresar la cantidad de elementos del conjunto U: "))

U = set()
for i in range(cantidad_u):
    U.add(int(input("Elemento " + str(i+1) + ': ')))

print(U)

cantidad_a = int(input("Ingresar la cantidad de elementos del conjunto A: "))


A = set()
for l in range(cantidad_a):
    A.add(int(input("Elemento " + str(l+1) + ': ')))

print(A)

if(A <= U):
    print("Conjunto A es subconjunto de U.")
    print("(U ⋃ A) ⋂ A:")
    print(((U|A)&A))
    print("(U ⋂ A) ⨁ A:")
    print(((U&A)^A))
    print("(U − A) ⨁ A:")
    print(((U-A)^A))
else:
    print("El conjunto A no es subconjunto de U, por ende, no se puede realizar las operaciones.")