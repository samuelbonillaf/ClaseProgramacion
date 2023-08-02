"""
saludo = "Hola mundo"
print(saludo)

nombre = input("Como te llamas?")
print("Hola" + nombre)

import math
a=((3+2)/(2*5))**2
print(a) 

Horas=float(input("Cuantas horas ha trabajado:"))
Precio=float(input("Pago por hora en pesos argentinos:"))
texto=str(Horas*Precio)
print("Le van a pagar"+texto+ "una completa miseria.")
"""
n=int(input("Deme un numero"))
#suma=(n*(n+1))/2
#print(suma)
res=0
for s in range (0, n+1):
  res+=s
print(res)

