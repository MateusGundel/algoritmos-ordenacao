from random import randint
from time import time
import sys
sys.setrecursionlimit(1000000)

class OrdernarVetores ():

    def __init__(self, min_range=10_000, max_range=100_000, show_base_vector=True, show_ordered_vectors=True):
        self.max_range = max_range
        self.min_range = min_range
        self.show_base_vector = show_base_vector
        self.show_ordered_vectors = show_ordered_vectors

        self.criar_vetor()

        self.selection_sort(self.vetor)

        self.insertion_sort(self.vetor)

        print("------- Merge Sort Iniciado -------")
        tempo_inicial = time()
        items_temp = self.merge_sort(self.vetor)
        if self.show_ordered_vectors:
            print(
                f'\nVetor Ordenado: {items_temp}\nTempo: {time()-tempo_inicial}\n')
        else:
            print(f'\nTempo: {time()-tempo_inicial}\n')

        print("------- Quick Sort Iniciado -------")
        tempo_inicial = time()
        items_temp = self.quick_sort(self.vetor)
        if self.show_ordered_vectors:
            print(
                f'\nVetor Ordenado: {items_temp}\nTempo: {time()-tempo_inicial}\n')
        else:
            print(f'\nTempo: {time()-tempo_inicial}\n')

    def criar_vetor(self):
        print("------- Criando o vetor -------")

        self.vetor = []

        for i in range(randint(self.min_range, self.max_range)):
            self.vetor.append(randint(0, 200_000))

        if self.show_ordered_vectors:
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
        if self.show_ordered_vectors:
            print(f'\nVetor Ordenado: {items}\nTempo: {time()-tempo_inicial}\n')
        else:
            print(f'\nTempo: {time()-tempo_inicial}\n')


    def insertion_sort(self, items):
        print("------- Insertion Sort Iniciado -------")
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

        if self.show_ordered_vectors:
            print(
                f'\nVetor Ordenado: {items}\nTempo: {time()-tempo_inicial}\n')
        else:
            print(f'\nTempo: {time()-tempo_inicial}\n')

    def merge(self, left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    def merge_sort(self, items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2

        left_list = self.merge_sort(items[:mid])
        right_list = self.merge_sort(items[mid:])

        return self.merge(left_list, right_list)

    def quick_sort(self, items):
        less = []
        equal = []
        greater = []

        if len(items) > 1:
            pivot = items[0]
            for x in items:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return self.quick_sort(less)+equal+self.quick_sort(greater)
        else:
            return items
