# Solicita ao usuário que insira um número
numero = int(input("Por favor, insira um número: "))

# Utiliza um laço for para percorrer o intervalo de 1 a 10
for i in range(1, 10):
    # Calcula a multiplicação do número fornecido pelo valor atual do laço
    produto = numero * i
    
    # Imprime cada produto em uma nova linha
    print(produto)
