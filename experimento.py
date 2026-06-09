import random

tamanhos = [1000, 10000, 100000]
vetores = {}

for tamanho in tamanhos:
    vetores[tamanho] = [
        random.randint(1, 1000000)
        for _ in range(tamanho)
    ]

print("Vetores gerados com sucesso!\n")

for tamanho in tamanhos:
    print(f"Vetor de {tamanho} elementos criado")

#Implementando o Bubble Sort
def bubble_sort(vetor):
    trocas = 0
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):

            if vetor[j] > vetor[j + 1]:

                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

                trocas += 1

    return vetor, trocas

# Teste do Bubble Sort
vetor_teste = [5, 3, 8, 1, 2]

ordenado, trocas = bubble_sort(vetor_teste.copy())

print("\nTeste Bubble Sort")
print("Vetor ordenado:", ordenado)
print("Quantidade de trocas:", trocas)    