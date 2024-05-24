
pares = 0
impares = 0 

numero = int(input("insira um numero"))
while numero !=0:
   temp = numero
   numero = int(input("insira um numero"))
   if temp % 2 == 0 :
      pares = pares+1
   else:
      impares = impares+1
print("quantidade de numeros pares:",pares)
print("quantidade de numeros impares:",impares)