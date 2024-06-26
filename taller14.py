#Brayan Steven León Martinez - Taller 14 - Matemáticas Computacional

print("Parte 1")

def solicitar_vector(longitud):
    vector = []
    for i in range(longitud):
        valor = float(input(f"Introduce el valor {i + 1} del vector: "))
        vector.append(valor)
    return vector

def producto_escalar(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

n = int(input("Introduce la longitud de los vectores: "))

print("Datos para el primer vector:")
vector1 = solicitar_vector(n)
print("Datos para el segundo vector:")
vector2 = solicitar_vector(n)

resultado = producto_escalar(vector1, vector2)
print(f"El producto escalar de los vectores es: {resultado}")

print("Parte 2")

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Introduce el elemento [{i+1}, {j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def escalar_por_matriz(escalar, matriz):
    return [[escalar * elemento for elemento in fila] for fila in matriz]

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    resultado = []
    for i in range(len(A)):
        fila_resultado = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

filas_A = int(input("Introduce el número de filas de la matriz A: "))
columnas_A = int(input("Introduce el número de columnas de la matriz A: "))
filas_B = int(input("Introduce el número de filas de la matriz B: "))
columnas_B = int(input("Introduce el número de columnas de la matriz B: "))

print("Datos para la matriz A:")
A = crear_matriz(filas_A, columnas_A)
print("Datos para la matriz B:")
B = crear_matriz(filas_B, columnas_B)

if filas_A == filas_B and columnas_A == columnas_B:
    print("3A:", escalar_por_matriz(3, A))
    print("4B:", escalar_por_matriz(4, B))
    print("A + B:", sumar_matrices(A, B))
else:
    print("No es posible sumar las matrices debido a diferencias en sus dimensiones.")

if columnas_A == filas_B:
    print("B × A:", multiplicar_matrices(B, A))
else:
    print("No es posible multiplicar B × A debido a diferencias en sus dimensiones.")

