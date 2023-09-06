# Очередь - это структура данных, которая работает по принципу
# "первым вошел, первым вышел" (First-In-First-Out, FIFO).
# Элементы добавляются в конец очереди, а извлекаются из начала.
# Это означает, что элементы обрабатываются в порядке их добавления.

# Просто - элементы добавляются в конец, извлекаются из начала.
class Queue:
    def __init__(self):
        self.items = []

    # Добавляет элемент в конец очереди (хвост).
    def enqueue(self, value):
        self.items.append(value)

    # Удаляет и возвращает элемент из начала очереди (головы).
    def dequeue(self):
        self.items.pop(0)

    # Возвращает элемент из начала очереди без его удаления.
    def peek(self):
        return self.items[0]

    # Проверяет, пуста ли очередь
    def is_empty(self):
        return len(self.items) == 0

    # возвращает кол-во элементов в очереди
    def get_size(self):
        return len(self.items)

    # Удаляет все элементы из очереди, делая её пустой.
    def clear(self):
        self.items.clear()

    # Преобразует очередь в массив.
    def to_array(self):
        return self.items

    # Инициализирует очередь элементами из массива.
    def init_from_array(self, array):
        for i in range(len(array)):
            self.items.append(array[i])

    # Инициализирует очередь элементами из связного списка.
    def init_from_linked_list(self, linked_list):
        current = linked_list.head.next
        while current:
            self.items.append(current.value)
            current = current.next

    # для красивого вывода содержимого очереди
    def __str__(self):
        return "Front " + str(self.items) + " Rear"