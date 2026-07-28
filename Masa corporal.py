# 1. Pedir los datos al usuario
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros (ej. 1.75): "))

# 2. Calcular el IMC (Fórmula: peso / altura al cuadrado)
imc = peso / (altura ** 2)

# 3. Imprimir el resultado en pantalla
print(f"El Índice de Masa Corporal (IMC) es: {imc:.2f}")
