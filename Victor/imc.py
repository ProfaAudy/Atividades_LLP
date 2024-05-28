altura = float(input("coloque a altura"))
peso = float(input("coloque o peso"))
imc =float (peso / (altura*altura))
if imc <18.5:
    print("abaixo do peso")
if imc <24.9 or imc== 18.5:
    print("peso normal")
if imc <29.9 or imc ==24.9:
    print("sobre peso")
if imc <34.9 or imc ==30:
    print("obesidade de grau 1")
if imc <39.9 or imc ==35:
    print("obesidade de grau 2")
if imc >40 or imc ==40:
    print("obesidade de grau 3 ou morbida")