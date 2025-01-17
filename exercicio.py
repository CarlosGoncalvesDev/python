# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Cadu', 'Bárbara', 'Heuller', 'Eliette']
anos = [2002, 2024]

# Para percorrer todos os itens de uma lista com o loop for, você pode usar essa estrutura:
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)

# Para fazer calculo da soma dos números impares de 1 a 10, você pode utilizar o seguinte código:
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

# Para imprimir os números de 1 a 10 de forma decrescente, você pode utilizar a seguinte estrutura:
for i in range(10, 0, -1):
    print(i)

# Para fazer uma tabuada interativa, você pode seguir o seguinte código:
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

# Uma possível resolução para fazer a soma dos elementos de uma lista com for e usar try except para validar, está no código a seguir:

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Um modo de solucionar essa questão com uma validação de lista vazia é do seguinte modo:
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")