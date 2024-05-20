n = int(input("insira seu peso"))

nu = int(input("Insira sua altura"))

imc = n / (nu*nu)

if imc < 18.5:
    print("Seu imc é", imc, "Abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print(" Seu imc é", imc, "Peso normal")
elif imc >=24.9 and imc < 29.9:
    print("Seu imc é", imc, "Sobrepeso")
elif imc > 30 and imc < 34.9:
    print("Seu imc é", imc, "Obesidade grau I")
elif imc > 35 and imc < 39.9:
    print("Seu imc é", imc, "Obesidade grau II")
else imc > 40: