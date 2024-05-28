peso = float(input("seu peso em quilograma"))
altura = float(input("altura em metros"))

# Calcule o IMC
imc = peso / (altura **2)

# Informa o valor do IMC
print("seu IMC e:")

if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("peso normal")
elif 25 <= imc< 29.9:
    print("sobrepeso")
elif 30 <= imc < 34.9:
    print("obesidade de grau 1")
elif 35 <= imc < 39.9:
    print("obesidade grau 2")
else:print("obesidade grau 3 ou morbida")
