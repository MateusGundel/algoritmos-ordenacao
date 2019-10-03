from random import randint
from time import time

class OrdernarVetores ():
    vetor = []
    MAX_RANGE = 100_000
    MIN_RANGE = 10_000

    def __init__(self):
        self.criar_vetor()

        self.selection_sort(self.vetor)

        self.insertion_sort(self.vetor)

        self.merge_sort(self.vetor)

        self.split_sort(self.vetor)

    def criar_vetor(self):
        print("------- Criando o vetor -------")

        self.vetor = []

        for i in range(randint(self.MIN_RANGE, self.MAX_RANGE)):
            self.vetor.append(randint(0, 9))

        print(f'Novo vetor:\n{self.vetor}\n')

    def selection_sort(self, items):
        print("------- Selection Sort Iniciado -------")
        tempo_inicial = time()

        # Não é necessário #iterar no último item (items[:-1] ignora o último elemento do array)
        for index, item in enumerate(items[:-1]):
            smallest_index = index  # considera o valor do índice mais
            # baixo o índice item que está iterando no primeiro loop
            for index_to_compare, item_to_compare in enumerate(
                    # itera somente os itens à #direita do índice
                    items[index::], index
            ):
                if item_to_compare < items[smallest_index]:
                    smallest_index = index_to_compare
            items[index], items[smallest_index] = (
                items[smallest_index],
                items[index]
            )  # Por fim, faz a troca de posição dos itens: o menor #encontrado com o item que está sendo iterado.
        print(f'\nVetor Ordenado: {items}\nTempo: {time()-tempo_inicial}\n')

    def insertion_sort(self, items):
        print("------- Selection Sort Iniciado -------")
        tempo_inicial = time()

        # Traverse through 1 to len(arr)
        for i in range(1, len(items)):

            key = items[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < items[j]:
                items[j+1] = items[j]
                j -= 1
            items[j+1] = key

        print(f'\nVetor Ordenado: {items}\nTempo: {time()-tempo_inicial}\n')

    def merge_sort(self, items):
        print("------- Merge Sort Iniciado -------")
        tempo_inicial = time()

        print(f'\nVetor Ordenado: {items}\nTempo: {time()-tempo_inicial}\n')

    def split_sort(self, items):
        print("------- Split Sort Iniciado -------")
        tempo_inicial = time()

        print(f'\nVetor Ordenado: {items}\nTempo: {time()-tempo_inicial}\n')
