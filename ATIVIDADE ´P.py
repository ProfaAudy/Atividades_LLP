# Inicializa as variáveis de contagem
pares = 0
impares = 0
 
# Loop para ler os números e contar os pares e ímpares
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
 
# Exibe o resultado
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")