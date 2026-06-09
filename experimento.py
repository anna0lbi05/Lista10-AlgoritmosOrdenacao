import random
import time
import statistics
import matplotlib.pyplot as plt

random.seed(42)

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

# Função para executar os testes
def executar_teste(nome_algoritmo, funcao_algoritmo, vetor):
    tempos = []
    movimentacoes = 0

    for _ in range(3):
        copia_vetor = vetor.copy()

        inicio = time.perf_counter()

        _, movimentacoes = funcao_algoritmo(copia_vetor)

        fim = time.perf_counter()

        tempos.append(fim - inicio)

    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)

    print("\n" + "=" * 60)
    print(f"Algoritmo: {nome_algoritmo}")
    print(f"Tamanho do vetor: {len(vetor)}")

    for i, tempo in enumerate(tempos, start=1):
        print(f"Execução {i}: {tempo:.6f} s")

    print(f"Tempo médio: {media:.6f} s")
    print(f"Desvio padrão: {desvio:.6f} s")
    print(f"Trocas/Movimentações: {movimentacoes}")


print("\nINICIANDO EXPERIMENTOS\n")

algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
    ("Heap Sort", heap_sort)
]

for tamanho in tamanhos:

    print(f"\nTESTANDO VETOR COM {tamanho} ELEMENTOS\n")

    for nome, funcao in algoritmos:

        if nome == "Bubble Sort" and tamanho == 100000:

            print("\n" + "=" * 60)
            print("Algoritmo: Bubble Sort")
            print("Tamanho do vetor: 100000")
            print("Execução 1: N/C")
            print("Execução 2: N/C")
            print("Execução 3: N/C")
            print("Tempo médio: N/A")
            print("Desvio padrão: N/A")
            print("Trocas/Movimentações: N/A")

            continue

        executar_teste(
            nome,
            funcao,
            vetores[tamanho]
        )

# Grafico comparativo
tamanhos_bubble = [1000, 10000]
bubble = [0.067327, 9.179487]

tamanhos_merge = [1000, 10000, 100000]
merge = [0.002681, 0.067035, 0.687877]

tamanhos_heap = [1000, 10000, 100000]
heap = [0.003858, 0.080653, 0.923093]

plt.figure(figsize=(10, 6))

plt.plot(
    tamanhos_bubble,
    bubble,
    marker='o',
    label='Bubble Sort'
)

plt.plot(
    tamanhos_merge,
    merge,
    marker='o',
    label='Merge Sort'
)

plt.plot(
    tamanhos_heap,
    heap,
    marker='o',
    label='Heap Sort'
)

plt.title('Comparação de Tempo dos Algoritmos')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo Médio (s)')

plt.legend()

plt.grid(True)

plt.xscale('log')
plt.yscale('log')

plt.show()