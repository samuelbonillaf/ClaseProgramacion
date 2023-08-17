def div (N1, N2):
  if N2!=0:
    Res=N1/N2
    return Res
  else:
    print("No se divide por 0")
    return 111
def mul (N1, N2):
  Res=N1*N2
  return Res
def sum (N1, N2):
  Res=N1+N2
  return Res
def res (N1, N2):
  Res=N1-N2
  return Res
  
NumeroA=float(input("Numero 1:"))
NumeroB=float(input("Numero 2:"))

dec=input("Que operacion desea realizar: + para suma \n 2 para resta \n 3 para multiplicacion \n 4 para division")
if dec==1:
  sum(NumeroA, NumeroB)
elif dec==2:
  res(NumeroA, NumeroB)
elif dec==3:
  mul(NumeroA, NumeroB)
elif dec==4:
  div(NumeroA, NumeroB)
else:
  print("Esa no es una seleccion") 


print(div(NumeroA, NumeroB))