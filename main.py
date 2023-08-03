"""
N = int(input("Ingrese un numero"))
M = int(input("Ingrese un numero"))
SU=M/N
print(round(SU, 3))

Inversion=float(input("Inversion:"))
Interes=float(input("Interes:"))
Tiempo=float(input("Tiempo en años"))
Valor=Inversion*(Interes/100+1)**Tiempo
print("Valor total", Valor)
"""
Payaso=int(input("Cuantos payasos:"))
Muñecas=int(input("Cuantas muñecas:"))
Peso=(Payaso*112)+(Muñecas*75)
print("El paquete va a pesar: ", Peso)