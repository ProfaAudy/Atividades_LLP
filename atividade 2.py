#print ("Para saber a media de 4 números")
#numero1 = int(input("coloque o primeiro número:"))
#numero2 = int(input("coloque o segundo número:"))
#numero3 = int(input("coloque o terceiro número:"))
#numero4 = int(input("coloque o quarto número:"))
#Media = ((numero1+numero2+numero3+numero4)/4)
#print("Media desses números é",Media)
def divisivel_por_cinco(numero):
    if numero % 5 == 0:
        return True
    else:
        return False
 
numero = int(input("Digite um número: "))
 
if divisivel_por_cinco(numero):
    print(f"O número {numero} é divisível por cinco.")
else:
    print(f"O número {numero} não é divisível por cinco.")
