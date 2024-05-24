#Condições
n = int(input("Insira um número: ")) 
# > maior que 
if n >= 60:
    print ("Pessoa idosa")
elif n >= 18:
    print("Maior de idade")
elif n >= 10:
    print("Adolecente")
elif n >= 0:
    print("Criança")
else:
    print("Nada")


if n== 55*48:
    print("Igual")
if n != 40: 
    print("Diferente")
if n >= 45:
    print("Maior ou igual")
if n <= 35*3:
    print("Menor ou igual")
if n > 78:
    print("Maior")
if n < 100:
    print("Menor")

if n < 4 and n > 1: 
    print("Número menor que 4 E maior que 1")
if n >= 10 or n >= 5:
    print("Número maior ou igual a 10 OU maior ou igual a 5")
if n % 2 != 1:
    print("Número ímpar")
