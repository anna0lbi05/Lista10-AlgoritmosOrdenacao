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

#Implementando o Merge Sort
def merge_sort(vetor):
    movimentacoes = [0]

    def merge_sort_rec(lista):
        if len(lista) <= 1:
            return lista

        meio = len(lista) // 2

        esquerda = merge_sort_rec(lista[:meio])
        direita = merge_sort_rec(lista[meio:])

        return merge(esquerda, direita)

    def merge(esquerda, direita):
        resultado = []

        i = 0
        j = 0

        while i < len(esquerda) and j < len(direita):

            if esquerda[i] < direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

            movimentacoes[0] += 1

        while i < len(esquerda):
            resultado.append(esquerda[i])
            i += 1
            movimentacoes[0] += 1

        while j < len(direita):
            resultado.append(direita[j])
            j += 1
            movimentacoes[0] += 1

        return resultado

    vetor_ordenado = merge_sort_rec(vetor)

    return vetor_ordenado, movimentacoes[0]

# Teste do Merge Sort
ordenado_merge, mov_merge = merge_sort(vetor_teste.copy())

print("\nTeste Merge Sort")
print("Vetor ordenado:", ordenado_merge)
print("Quantidade de movimentações:", mov_merge)

#Implementando o Heap Sort
def heapify(vetor, n, i, movimentacoes):
    maior = i

    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and vetor[esquerda] > vetor[maior]:
        maior = esquerda

    if direita < n and vetor[direita] > vetor[maior]:
        maior = direita

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]

        movimentacoes[0] += 1

        heapify(vetor, n, maior, movimentacoes)


def heap_sort(vetor):
    movimentacoes = [0]

    n = len(vetor)

    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i, movimentacoes)

    for i in range(n - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]

        movimentacoes[0] += 1

        heapify(vetor, i, 0, movimentacoes)

    return vetor, movimentacoes[0]

# Teste do Heap Sort
ordenado_heap, mov_heap = heap_sort(vetor_teste.copy())

print("\nTeste Heap Sort")
print("Vetor ordenado:", ordenado_heap)
print("Quantidade de movimentações:", mov_heap)