
# Inicializa contadores
cont_pares = 0
cont_impares = 0

# Loop para ler números até que o valor zero seja inserido
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

# Exibe os resultados
print(f"Quantidade de números pares: {cont_pares}")
print(f"Quantidade de números ímpares: {cont_impares}")